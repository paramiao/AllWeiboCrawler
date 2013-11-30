#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
from CrawlerDriver import CrawlerDriver


from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)
define("tencent_username", help="腾讯微博用户名",
               default=None)
define("tencent_password", help="腾讯微博密码",
               default=None)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/test', TestHandler),
            (r'/weibos', WeibosHandler),
        ]
        settings = dict(
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.crawl_driver = CrawlerDriver()


class BaseHandler(tornado.web.RequestHandler):
    @property
    def crawl_driver(self): 
        return self.application.crawl_driver


class TestHandler(BaseHandler):
    def get(self):
        self.write('Hello World')


class WeibosHandler(BaseHandler):
    def get(self):
        weibo_type = self.get_argument('site', '新浪')
        page = self.get_argument('page', 1)
        keyword = self.get_argument('kw', '比特币')
        count = self.get_argument('limit', 10)
        self.crawl_driver.setWeiboCrawler(weibo_type.encode('utf8'), options.tencent_username, options.tencent_password)
        result = self.crawl_driver.getWeibos(keyword, page, count)
        self.write(tornado.escape.json_encode(result))


def main():
    tornado.options.parse_command_line()
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(io_loop)
    io_loop.start()


if __name__ == '__main__':
    main()
