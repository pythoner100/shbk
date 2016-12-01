#coding:utf8
import tornado.web
import torndb


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        db = torndb.Connection(host="localhost", user="root", password="11111111", database="shbk")
        classs = db.query("select * from class")
        print classs
        self.render('index.html',classs=classs)

class HotHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('hot handler ') 
        self.render('hot.html') 

class HourHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hour.html")
    
class ChartHandler(tornado.web.RequestHandler):
    def get(self):
       # db = torndb.Connection(host="localhost",database="shbk", user="root", password="11111111")
       # commenttables = db.query("select * from commenttable")
       # print commenttables
        self.render("chart.html")

class WordHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("word.html")


