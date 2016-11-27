import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class HotHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hot handler ')
