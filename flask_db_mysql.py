# 此项目使用flask框架实现对数据库的操作 可在pipenv下实现数据库的迁移，建立表结构
from helloflask import app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy(app)


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class Country(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    capitals=db.relationship('Capital',backref='country')
    def __repr__(self):
        return 'Country:{}'.format(self.name)

class Capital(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),unique=True)
    population=db.Column(db.Integer)
    country_id=db.Column(db.Integer,db.ForeignKey('country.id'))

    def __repr__(self):
        return 'Capital:{}'.format(self.name)



if __name__=='__main__':

    db.drop_all()
    db.create_all()
    c1=Country(name='China')
    c2=Country(name='UK')           #c1,c2数据库country table添加数据
    ca1=Capital(name='beijing')
    ca2 = Capital(name='london')    #ca1,ca2数据库capital table添加数据
    ca1.country = c1                #table ca1和table c1建立关系
    ca2.country=c2                  #table ca2和table c2建立关系
    # db.session.add_all([c1,c2,ca1,ca2])     #添加数据
    # db.session.commit()                     #提交数据到数据库
    print('中国的首都是：{},英国的首都是：{}'.format(c1.capitals,c2.capitals) )         #查看 对应表属性是否生效
    print('北京位于：{},伦敦位于：{}'.format(ca1.country,ca2.country))
    print('记录China对应的id是：{},记录UK对应的id是：{}'.format(ca1.country_id,ca2.country_id))















