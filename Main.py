#-*-coding:utf-8-*-
from flask import Flask, request, render_template, redirect, url_for, session, g, escape, flash, jsonify
# from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler
import config
from extension import db
import os, json, datetime, random, uuid
from models import Register  # 数据库表
from werkzeug.utils import secure_filename
# from werkzeug.security import generate_password_hash, check_password_hash   # 加密


app = Flask(__name__)
# app. secret_key= 'ning'
app.config.from_object(config)
db.init_app(app)

# 主页
@app.route('/')
def index():
    return "H"
    # return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

