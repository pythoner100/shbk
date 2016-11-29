import tornado.web

class ArticleCreateHandler(tornado.web.RequestHandler):
    def post(self):
        conent = self.get_argument("content")
        print content
