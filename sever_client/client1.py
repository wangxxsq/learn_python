# -*- coding: utf-8 -*-
# tornado_test1.ppt任务
import tornado.httpclient
import tornado.httpserver
import tornado.web
import tornado.gen
import tornado.options
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPClient,AsyncHTTPClient


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
        self.port = 4001


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('1处理中。。。')
        http_client = AsyncHTTPClient()
        url = 'http://127.0.0.1:4002/tornado1'

        response = yield http_client.fetch(url, method='GET', request_timeout=120)
        response_body = response.body.decode('utf8')
        print(response_body)
        self.finish(response_body)


class Main2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('2处理中。。。')
        http_client = AsyncHTTPClient()
        url = 'http://127.0.0.1:4002/tornado2'

        response = yield http_client.fetch(url, method="GET", request_timeout=120)
        response_body = response.body.decode('utf8')
        print(response_body)
        self.finish(response_body)

if __name__ == '__main__':
    print("http://127.0.0.1:4001/tornado1")
    print("http://127.0.0.1:4001/tornado2")
    AsyncHTTPClient.configure(None, max_clients=200)
    application = Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()







