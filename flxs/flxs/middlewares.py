# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
from tkinter import Image
from flxs.超级 import Chaojiying_Client
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# useful for handling different item types with a single interface
from PIL import Image
from faker import Faker


class FlxsSpiderMiddleware:
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


class FlxsDownloaderMiddleware:
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
        ua = Faker()
        user_agent = ua.user_agent()
        request.headers['User_Agent'] = user_agent

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        if "验证码" in response.text:
            print("验证码")
            chrome_open = Options()
            chrome_open.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = webdriver.Chrome(options=chrome_open)
            c = request.url
            # print(c)
            driver.get(c)
            driver.maximize_window()
            time.sleep(3)
            """获取全部图片"""
            driver.save_screenshot("验证图片.png")
            """从全屏截图中扣识别验证码的图片,扣验证码的图片的方式就是先把验证码的图片定位出来,然后获取坐标,获取的坐标是验证码
               左上角的坐标,想要获取整个验证码的坐标,就要左上角加上图片的宽度跟高度,然后返回坐标,用Pil进行保存"""
            # 定位验证码图片位置
            img_meusare = driver.find_element(By.ID, 'img_verifyCode')
            # 获取验证码图标坐标信息,x值跟y值
            meusare = img_meusare.location
            # 返回字典格式的,这里要把值都取出来
            x, y = int(meusare["x"]), int(meusare["y"])
            # 获取验证码图片大小
            dic_x = img_meusare.size
            # 用左上角的坐标加上图片的宽度,加上图片的高度
            x1, y1 = x + dic_x["width"], y + dic_x["height"]
            zone = (x, y, x1, y1)
            # 打开图片
            pic = Image.open("验证图片.png")
            # 截图指定范围的内容,赋值给一个变量
            img = pic.crop((x, y, x1, y1))
            # 保存图片
            img.save("验证码图片.png")
            chaojiying = Chaojiying_Client('13278096476', 'lovewcy5210', '2004')
            # """传入获取的图片"""
            im = open('验证码图片.png', 'rb').read()
            dic_str = (chaojiying.PostPic(im, 2004))
            print(dic_str['pic_str'])
            time.sleep(3)
            driver.find_element(By.ID,'input_verifyCode').send_keys(dic_str['pic_str'])
            time.sleep(1)
            driver.find_element(By.CLASS_NAME,'valiate_code_btn').click()
            return request
        # print(response.text)

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
