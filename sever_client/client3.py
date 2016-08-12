# -*- coding: utf-8 -*-
import redis
import json
import tornado.httpclient
import tornado.httpserver
import tornado.web
import tornado.gen
from tornado.ioloop import IOLoop
import tornado.options
from tornado.httpclient import HTTPClient,AsyncHTTPClient
from urllib.parse import urlencode

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
        self.port = 6001


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        map = {"a": "1",
               "b": "2",
               "c": "3",}
        map1 = json.dumps(map)
        print(map1)
        print('1处理')
        response = None
        http_client = AsyncHTTPClient()
        url = 'http://127.0.0.1:6002/tornado1'
        try:
            response = yield http_client.fetch(url, method='POST', body=map1, request_timeout=120)
        except Exception as e:
            print(e)
        response_body = response.body
        print(response_body)


class Main2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        print('2处理')
        map = {"a": "1",
               "b": "2",
               "c": "3",
        }
        map2 = urlencode(map)

        htttp_client = AsyncHTTPClient()
        base_url = 'http://127.0.0.1:6002/tornado2'
        url = base_url + '?'+map2
        print(url)

        response = yield htttp_client.fetch(url, method='GET', request_timeout=120)
        response_body = response.body.decode('utf8')
        print(response_body)
        self.finish(response_body)

if __name__ == '__main__':
    print("http://127.0.0.1:6001/tornado1")
    print("http://127.0.0.1:6001/tornado2")
    AsyncHTTPClient.configure(None, max_clients=200)
    application = Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()




