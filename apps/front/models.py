from exts import db,ma
from flask_marshmallow import fields
from marshmallow import fields,Schema,pprint


class AreasModel(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    pid = db.Column(db.Integer,db.ForeignKey('areas.id'))
    districts = db.relationship('AreasModel',backref='area',remote_side=[id])


class AreaSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    districts = ma.Nested('self',only=('id','name'))

    class Meta:
        fields = ('id','name','districts')


# class AreaSchema(ma.ModelSchema):
#     districts = ma.Nested('self')
#     class Meta:
#         model = AreasModel
#         fields = ('id','name','districts')
    # area = ma.Nested('self',only=('id','name'))


area_schema = AreaSchema()
areas_schema = AreaSchema(many=True)

