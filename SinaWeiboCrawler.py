#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import hashlib
import random
from bs4 import BeautifulSoup
import urllib
import json
from WeiboCrawler import WeiboCrawler


class SinaWeiboCrawler(WeiboCrawler): 
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
            }

    #count最大为50
    def getWeibos(self, keyword,  page=1, count=10):
        url = 'http://m.weibo.cn/searchs/weibo?key=%s&page=%d&count=%d' % (keyword, page, count)
        result = WeiboCrawler.request(self, url, self.headers)
        if 'result' in result and result['result']:
            infos = result['info']
            json_infos = json.loads(infos)
            if 'ok' in json_infos and json_infos['ok']:
                return_val = {'total_count': json_infos['total_number'], 'total_pages': json_infos['maxPage'], 'msgs': []}
                msgs = json_infos['mblogList']
                return_val['msgs'] = msgs
                return return_val

if __name__ == '__main__':
    sw = SinaWeiboCrawler()
    print sw.getWeibos(u'比特币', 2, 5)
