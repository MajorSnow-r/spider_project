# Scrapy settings for flxs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'flxs'
REDIS_ITEMS_SERIALIZER = 'scrapy_redis.picklecompat.pickle'
REDIS_OVERALL_SERIALIZER = 'scrapy_redis.picklecompat.pickle'
SPIDER_MODULES = ['flxs.spiders']
NEWSPIDER_MODULE = 'flxs.spiders'


"""调度器,使用scrapy-redis"""
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
"""去重的 使用scrapy-redis"""
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
"""断点续爬"""
SCHEDULER_PERSIST = True


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'flxs (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = "WARNING"
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Cookie': 'host4chongzhi=https%3a%2f%2fcn.bing.com%2f; Hm_lvt_6d308f6626f6d0864b6bb4f348f2b5e5=1676603468; readline=1; fontFamily=1; fontsize=16; vip_img_width=3; font_Color=666666; KeenFire=UMID=26632802&UserID=13278096476&Pwd=0cef1961e206992144acdadc29f6721b&Identity=web44975.0619563845&PhotoID=0&NickName=AAA%40...; UU12345678=uuc=133210875192801198527434912; comment_reply=0; nc_rela=38; novelrelative=1262306; favorates28=1262306%2C1%7C1268637%2C1%7C1271504%2C6%7C1251025%2C20%7C1271136%2C4%7C1263497%2C8%7C1262487%2C4%7C1258234%2C3%7C1265686%2C3%7C1263609%2C1%7C1266578%2C2%7C1260075%2C2%7C1269915%2C1%7C1271818%2C1%7C1265257%2C1%7C1270410%2C2; autobuychapters28=1262306%2C1%7C1268637%2C1%7C1271504%2C6%7C1251025%2C20%7C1271136%2C4%7C1263497%2C8%7C1262487%2C4%7C1258234%2C3%7C1265686%2C3%7C1263609%2C1%7C1266578%2C2%7C1260075%2C2%7C1269915%2C1%7C1271818%2C1%7C1265257%2C1%7C1270410%2C2; curr_url=https%3A//b.faloo.com/1262306_2.html; Hm_lpvt_6d308f6626f6d0864b6bb4f348f2b5e5=1676613956; bgcolor=%23FFFFFE'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'flxs.middlewares.FlxsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'flxs.middlewares.FlxsDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'flxs.pipelines.FlxsPipeline': 300,
   'flxs.pipelines.MongdbPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
