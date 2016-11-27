import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class HotHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hot handler ')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hot", HotHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5002)
    tornado.ioloop.IOLoop.current().start()
