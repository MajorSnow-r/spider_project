# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json
from scrapy import signals
from faker import Faker
import requests
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ShjdSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ShjdDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class changeUAMiddleware:
    def process_request(self, request, spider):
        f = Faker()
        user = f.user_agent()
        request.headers["User-Agent"] = user


class ChangeIPMideeleware:
    def __init__(self):
        # 账号密码
        self.username = "d4205257060"
        self.password = "tkcj9gix"
        # api_url
        # self.api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=okrqtkv9pd6imvhfv28v&num=2&signature=d7o1u1k1ta1o73n1uhsrfsrur4aj6qz3&pt=1&format=json&sep=1"
        self.api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=okrqtkv9pd6imvhfv28v&num=2&signature=d7o1u1k1ta1o73n1uhsrfsrur4aj6qz3&pt=1&format=json&sep=1"
        # 测试ip是否可以用的网站
        self.ceurl = "https://www.baidu.com/"
        self.ip_list = []
        # 初始化一个数字用来计数现在的ip数量
        self.ip_count = 0
        # 初始化一个数字用来控制ip使用次数
        self.count = 0

    # 搭建ip池
    def getIPData(self):
        response = requests.get(self.api_url).text
        # print(response)
        self.ip_list.clear()
        """解析出来ip数据"""
        for ip in json.loads(response)["data"]["proxy_list"]:
            # print("获取的ip为:", ip)
            self.ip_list.append(ip.strip("'"))

    # 携带代理ip发送请求
    def protrequest(self, request):
        self.proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.username, "pwd": self.password,
                                                            "proxy": self.ip_list[self.ip_count - 1]},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.username, "pwd": self.password,
                                                             "proxy": self.ip_list[self.ip_count - 1]}
        }
        request.meta["proxy"] = self.proxies["https"]

    def jiaoyan(self):
        requests.get(url="https://dev.kdlapi.com/testproxy", proxies=self.proxies, timeout=1)

    """判断ip是否可以正常使用"""

    def jiaoyans(self, request):
        try:
            self.protrequest(request)
            self.jiaoyan()
        except:
            if self.ip_count == 0 or self.ip_count == 2:
                self.getIPData()
                self.ip_count = 1
                print("报错")
            """
            如果条件不满足,那么就让ip数自增一,然后在重新调用一下判断ip是否正常使用的方法,判断结束之后继续回到try里面在进行判断如果满足就往下执行
            如果还是不满足就在自增一,一直这么循环到满足为止。
            """
            self.ip_count = self.ip_count + 1
            """自己调用自己"""
            self.jiaoyans(request)

    def process_request(self, request, spider):
        """
        如果ip现在的数量是0,那么就证明是没有ip池的满足条件调用搭建ip池的函数,因为获取ip最大数字是2所以当计数ip等等于5的时候
        也要重新搭建一个新的ip池
        """
        if self.ip_count == 0 or self.ip_count == 2:
            self.getIPData()
            self.ip_count = 1
        """
        判断ip访问次数,如果ip访问超过3次了,那么就让换一个ip去进行访问,满足条件访问ip次数清空为0
        如果不满足条件就证明访问ip次数还没有达到3次,那么就继续使用加1
        """
        if self.count == 4:
            self.ip_count = self.ip_count + 1
            self.count = 0
        else:
            self.count = self.count + 1
        self.jiaoyans(request)


class ChangeIFMiddleware:
    def process_response(self, request, response, spider):
        print(response.status)
        if response.status not in [200,201]:
            print("更换ip")
            api = "https://dps.kdlapi.com/api/getdps/?secret_id=okrqtkv9pd6imvhfv28v&num=1&signature=d7o1u1k1ta1o73n1uhsrfsrur4aj6qz3&pt=1&format=json&sep=1"
            response = requests.get(api).text
            for ip in json.loads(response)["data"]["proxy_list"]:
                username = "d4205257060"
                password = "tkcj9gix"
                proxies = {
                    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                    "proxy": ip},
                    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                     "proxy": ip}
                }
                request.meta["proxy"] = proxies["https"]
                return request
        return response


