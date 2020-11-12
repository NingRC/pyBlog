#-*-coding:utf-8-*-
# 配置文件
import os
DEBUG = True
SECRET_KEY=os.urandom(24)
# dialect+driver://username:password@port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
# 数据库名
USERNAME = 'root'
# 数据库密码
PASSWORD = '12345678'
#host服务器的主机名，本地127.0.0.1
HOST = '127.0.0.1'
#port,项目主运行程序的端口号
PORT = '3306'
#database.mysql客户端已添加数据库名
DATABASE = 'myflask'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.\
    format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
