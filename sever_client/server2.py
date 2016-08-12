# -*- coding: utf-8 -*-
# 发送接收数据
import json
import tornado.gen
import tornado.web
import tornado.httpserver
import tornado.httpclient
import tornado.options
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/tornado1", MainHandler),
            (r"/tornado2", Main2Handler),
        ]

        settings = dict(
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.port = 5002


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        print('1处理')
        body = self.request.body.decode()
        body = json.loads(body)  # json方式取
        print(body)
        # a = self.get_body_argument('a')    #url方式取
        # print(a)


class Main2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('2处理。。')
        a = self.get_argument('a')
        print(a)


if __name__ == '__main__':
    print('http://127.0.0.1:5002/tornado1')
    print('http://127.0.0.1:5002/tornado2')
    AsyncHTTPClient.configure(None, max_clients=200)
    application = Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()


