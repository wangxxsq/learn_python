# -*- coding: utf-8 -*-
# 数据保存到redis
import redis
import json
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.options
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

r = redis.Redis(host='localhost', port=6379, db=2)


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
        self.port = 6002


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        print('1处理')
        request_body = self.request.body.decode()
        request_body = json.loads(request_body)
        print(request_body)

        r.hset('map1','b','2')
        r.hmset('map',request_body)


class Main2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('2处理')

        a = self.get_argument('a')
        print(a)

        r.hset('map2', 'a','1')


if __name__ == '__main__':
    print("http://127.0.0.1:6002/tornado1")
    print("http://127.0.0.1:6002/tornado2")
    AsyncHTTPClient.configure(None, max_client=200)
    application = Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()
