#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import hashlib
import random
import json
from WeiboCrawler import WeiboCrawler


class TencentWeiboCrawler(WeiboCrawler):

    def __init__(self, username, password, isMD5=False):
        self.username = str(username)
        if isMD5:
            self.password = password
        else:
            self.password = hashlib.md5(password).hexdigest().upper()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
            }

    def getSid(self):
        url = 'http://pt.3g.qq.com/login?act=json&format=2&bid_code=microblogLogin&r=%f&qq=%s&pmd5=%s&go_url=http://ti.3g.qq.com/touch/iphone/index.jsp?g_f=18106' % (random.random(), self.username, self.password)
        result = WeiboCrawler.request(self, url, self.headers)
        if 'result' in result and result['result']:
            info = result['info'].replace('pt.handleLoginResult(', '')[:-2]
            json_info = json.loads(info)
            if len(json_info) == 8:
                sid = json_info[4]
                self.sid = sid
                return sid
        return None

    def getWeibos(self, keyword,  page=1, size=10, sid=None):
        if not sid:
            sid = self.sid
        url = 'http://ti.3g.qq.com/touch/s?sid=%s&aid=vaction&more=1&mst=33&ac=60&keyword=%s&dl2=1&dumpJSON=1&pageid=search&pid=%d&psize=%d' % (sid, keyword, page, size)
        result = WeiboCrawler.request(self, url, self.headers)
        if 'result' in result and result['result']:
            json_info = json.loads(result['info'])
            if 'result' in json_info and json_info['result'] == '0':
                msgs = json_info['jsonDump']['msgs']
                total_info = json_info['info']
                return {'msgs': msgs, 'total_pages': total_info['pageCount'], 'total_count': total_info['totalCount']}

if __name__ == '__main__':
    tw = TencentWeiboCrawler('USERNAME', 'PASSWORD')
    tw.getSid()
    print tw.getWeibos('比特币')
