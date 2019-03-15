# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, tornado")

urls = [
    (r"/", MainHandler),
]

if __name__ == "__main__":
    app = tornado.web.Application(urls)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
