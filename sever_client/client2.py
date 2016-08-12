# -*- coding: utf-8 -*-
# tornado_test2.ppt任务
import json
import tornado.gen
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.options
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from urllib.parse import urlencode


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
        self.port = 5001


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        map = {"a":"1",
               "b":"2",
               "c":"3"}
        map1 = json.dumps(map)      # json方式 {'a':'1'}
        print(map1)

        # map2 = urlencode(map)  #url方式  a=1&b=2
        # print(map2)

        print('1处理中。。。')
        http_client = AsyncHTTPClient()
        url = 'http://127.0.0.1:5002/tornado1'
        response = yield http_client.fetch(url, method='POST', body=map1, request_timeout=120)   #json方式
        # response = yield http_client.fetch(url, method='POST', body=map2, request_timeout=120)  #urlencode方式
        response_body = response.body.decode('utf8')
        print(response_body)
        self.finish(response_body)


class Main2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('2处理中。。。')

        map = {"a":"1",
               "b":"2",
               "c":"3",}

        # map1 = json.dumps(map)   #json 要用post方法，不能用get
        # print(map1)

        map2 = urlencode(map)
        print(map2)

        http_client = AsyncHTTPClient()
        base_url = 'http://127.0.0.1:5002/tornado2'
        url = base_url+'?'+map1
        print(url)

        response = yield http_client.fetch(url, method='GET', request_timeout=120)
        response_body = response.body.decode('utf8')
        print(response_body)
        self.finish(response_body)


if __name__ == '__main__':
    print("http://127.0.0.1:5001/tornado1")
    print("http://127.0.0.1:5001/tornado2")
    AsyncHTTPClient.configure(None, max_clients=200)
    application = Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()

