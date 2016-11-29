import tornado.web
import torndb


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        conn = torndb.Connection(host="localhost", user="root", password="11111111", database="shbk")
        articles = conn.query("select * from article")
        print articles
        self.render('index.html', articles=articles)

class HotHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('hot handler ') 
        self.render('hot.html') 

class HourHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hour.html")
    
class ChartHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chart.html")

class WordHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("word.html")


