#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import urllib
import traceback


class WeiboCrawler:

    def __init__(self):
        pass

    def request(self, url, headers=None, data=None):
        request = urllib2.Request(
            url=url,
            data=data,
            headers=headers
            )
        try:
            result = urllib2.urlopen(request).read()
            return {'result': True, 'info': result}
        except urllib2.HTTPError as e:
            errorinfo = e.read()
            return {'result': False, 'errorno':-1, 'msg': errorinfo}
        except:
            return {'result': False, 'errorno':-2, 'msg': traceback.format_exc()}
