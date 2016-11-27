import tornado.ioloop
import tornado.web
from handler.index import MainHandler, HotHandler,HourHandler
import os

def make_app():
    basedir = os.path.dirname(__file__)
    settings = {
        'debug': True,
        'template_path': os.path.join(basedir, 'template')
    }
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hot", HotHandler),
        (r"/hour",HourHandler)
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
