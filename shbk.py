import tornado.ioloop
import tornado.web
from handler.index import MainHandler, HotHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hot", HotHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5002)
    tornado.ioloop.IOLoop.current().start()
