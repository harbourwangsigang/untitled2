#coding:utf8
from baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
    def craw(self, root_url):
        pass


if __name__ == "__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)