import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render('index.html')

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
