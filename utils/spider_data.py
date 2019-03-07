import pymysql
import requests
from lxml import etree
import hashlib
from utils import dxcache
from flask import session

# 获取网页内容并生成md5值
class Spider(object):

    def __init__(self):
        self.headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://www.mca.gov.cn/article/sj/xzqh/2019/201903/20190300014983.shtml'
    }
        # self.url = "http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201902061009.html"
        self.url = "http://www.mca.gov.cn/article/sj/xzqh/2018/201804-12/201804121005.html"

    def check_update(self):
        resp = requests.get(self.url)
        m = hashlib.md5()
        m.update(resp.content)
        # 生成最新的md5值
        new_md5_key = m.hexdigest()
        # 从memcache 获取最新的md5值
        old_md5_key = dxcache.get('web_md5_key')
        # 如果相等,说明内容没发生变化,不用继续爬
        if old_md5_key and old_md5_key == new_md5_key:
            return False
        else:
            dxcache.set('web_md5_key', m.hexdigest(), timeout=60 * 60 * 24)
            return True

    def _get_data(self):
        resp = requests.get(self.url, headers=self.headers)
        html = etree.HTML(resp.text)
        trs = html.xpath("//div[@align='center']//tr")
        all_codes = []
        for tr in trs:
            code = tr.xpath("./td[2]/text()")
            name = tr.xpath('./td[3]/text()')
            if code:
                code = code[0]
                name = name[0]
                pid = code[:2] + '0000'
                all_codes.append({'code': code, 'name': name, 'pid': pid})
        return all_codes[1:]

    @staticmethod
    def _save_data(all_codes):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='mabao_test',
            charset='utf8'
        )
        cur = conn.cursor()
        #　异常处理
        try:
            for code_info in all_codes:
                sql = "insert into areas values ('%s','%s','%s')"
                cur.execute(sql % (code_info.get('code'), code_info.get('name'), code_info.get('pid')))
            conn.commit()
        except Exception as e:
            conn.rollback()


    def run(self):
        all_infos = self._get_data()
        self._save_data(all_infos)

