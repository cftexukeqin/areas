from marshmallow import Schema,fields,pprint
from datetime import datetime
from sqlalchemy import Column, Integer, String,DateTime
from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(DB_URI, echo=True)

# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()
        self.friends = []
        self.employer = None
    # name = Column(Integer,primary_key=True)
    # email = Column(String(100))
    # created_at = Column(DateTime)
    # friends = Column()

class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    friends = fields.Nested('self', many=True)
    # Use the 'exclude' argument to avoid infinite recursion
    employer = fields.Nested('self', exclude=('employer', ), default=None)

user = User("Steve", 'steve@example.com')
user.friends.append(User("Mike", 'mike@example.com'))
user.friends.append(User('Joe', 'joe@example.com'))
user.employer = User('Dirk', 'dirk@example.com')
result = UserSchema().dump(user)
pprint(result.data, indent=2)