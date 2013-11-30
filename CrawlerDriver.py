#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from TencentWeiboCrawler import TencentWeiboCrawler
from HexunWeiboCrawler import HexunWeiboCrawler
from SinaWeiboCrawler import SinaWeiboCrawler

class WeiboCrawlerDriver:

    def __init__(self):
        pass


    def setWeiboCrawler(self, name, username=None, password=None):
        parse_dict = {
            '腾讯': TencentWeiboCrawler,
            '和讯': HexunWeiboCrawler,
            '新浪': SinaWeiboCrawler
            }
        if name == '腾讯':
            self.weibo_crawler = parse_dict[name](username, password)
            self.weibo_crawler.getSid()
        else:
            self.weibo_crawler = parse_dict[name]()


    def getWeibos(self, keyword, page, count):
        return self.weibo_crawler.getWeibos(keyword, page, count)


if __name__ == '__main__':
    wcd = WeiboCrawlerDriver()
    wcd.setWeiboCrawler('腾讯', '腾讯帐号', '腾讯密码')
    wcd.setWeiboCrawler('新浪')
    wcd.setWeiboCrawler('和讯')
    print wcd.getWeibos('比特币', 1, 1)
