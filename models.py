#-*-coding:utf-8-*-

from extension import db

# 注册表单
class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #主键
    reusername = db.Column(db.String(100),nullable = False)    #名字
    reuserpwd = db.Column(db.String(100),nullable = False)   #密码
    reuseremail = db.Column(db.String(100),nullable = False)   #邮箱

