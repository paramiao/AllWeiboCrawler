AllWeiboCrawler
===============

腾讯，新浪，和讯等微博搜索公用库，


# 基本说明
* 腾讯需要用户名密码，新浪和和讯无需用户名密码
* 基本只用调用CrawlerDriver.py里面的CrawlerDriver里的通用方法即可，返回值中，
total_count——总数
msgs——微博列表
total_pages——总页数（以当前请求的count限制来计算，当前和讯微博不返回页数）
如：

```python

#实例化一个微博抓取对象
crawlDriver = CrawlerDriver()
#设置抓取的微博网站
crawlDriver.setWeiboCrawler('腾讯', '腾讯帐号', '腾讯密码')
crawlDriver.setWeiboCrawler('新浪')
crawlDriver.setWeiboCrawler('和讯')
#根据关键词搜索微博
crawlDriverw.getWeibos('比特币', 1, 1)

```
