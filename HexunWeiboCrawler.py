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


class HexunWeiboCrawler(WeiboCrawler): 
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
            }

    def getWeibos(self, keyword,  page=1):
        url = 'http://t.hexun.com/k/topic.html?type=1&value=%s&pg=%d' % (json.dumps(keyword).replace('\\', '%').replace('"', ''), page)
        result = WeiboCrawler.request(self, url, self.headers)
        if 'result' in result and result['result']:
            infos = result['info'].decode('gb2312')
            soup = BeautifulSoup(infos)
            total_soup = soup.select('.headerR1')[0]
            total_num = total_soup.get_text().split('共')[-1].split('条')[0].strip()
            return_val = {'total': int(total_num), 'msgs':[]}
            allmsgs = []
            msgs_soup = soup.select('.nr_con')
            for msg_soup in msgs_soup:
                avatar =  'http://t.hexun.com%s' % msg_soup.select('.nr_conLa > a')[0].get('href')
                nickandtext = msg_soup.select('.nr_shuo')[0].get_text().split('：')
                nickname = nickandtext[0]
                text = nickandtext[1]
                ts = msg_soup.select('.nr_tan > h3 > a')[0].get_text()
                allmsgs.append({
                    'avatar': avatar,
                    'nickname': nickname,
                    'text': text,
                    'datetime': ts,
                    })
            return_val['msgs'] = allmsgs
            return return_val

if __name__ == '__main__':
    hw = HexunWeiboCrawler()
    print hw.getWeibos(u'比特币', 2)
