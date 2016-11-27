#coding:utf8

import tornado.options
import tornado.web
import torndb

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        db = torndb.Connection(host = "localhost",database = "db_name",user = "root",password = "11111111")
        students = db.query("select * from shbk")
        self.render('index.html',students=students)
