# -*- coding: utf-8 -*-
# 发送接收数据
import time
import tornado.gen
import tornado.web
import tornado.options
import tornado.httpclient
import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


class Application(tornado.web.Application):
        def __init__(self):
            handlers = [
                (r"/tornado1", MainHandler),
                (r"/tornado2", Main2Handler),
            ]
            settings = dict(
                debug=True,
            )
            tornado.web.Application.__init__(self, handlers, **settings)
            self.port = 4002


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('1处理')
        yield tornado.gen.Task(IOLoop.instance().add_timeout, time.time() + 7)
        self.finish("Hello,Tornado1")


class Main2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('2处理')

        yield tornado.gen.Task(IOLoop.instance().add_timeout, time.time() + 7)
        self.finish(
            "Hello,Tornado2"
        )


if __name__ == "__main__":
    print("http://127.0.0.1:4002/tornado1")
    print("http://127.0.0.1:4002/tornado2")
    AsyncHTTPClient.configure(None, max_clients=200)
    application = Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()




