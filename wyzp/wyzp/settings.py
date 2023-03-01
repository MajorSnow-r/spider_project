# Scrapy settings for wyzp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wyzp'

LOG_LEVEL="WARNING"
SPIDER_MODULES = ['wyzp.spiders']
NEWSPIDER_MODULE = 'wyzp.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wyzp (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'cookie': 'hb_MA-9ADA-91BF1A6C9E06_source=cn.bing.com; HR163=0ef3cbbb5182c12805cf24829ed51ad791a5cc59; NTEShrSI=E13200FCC4DDF095318947416189C86B.hzabj-new-rms4.server.163.org-8011; hb_MA-8E16-605C3AFFE11F_source=zc.reg.163.com; hb_MA-AC55-420C68F83864_source=zc.reg.163.com; NTES_P_UTID=eaK06MnYnw67yz13EvJuRFwqZiemg9FM|1676275738; NTES_SESS=fierAycnqhPJCdSn4ZLhRdY6Tuxxx4RKLFDXPAKf.1g0Xu9MX1ahwn1usbh8RN3Vxz4tnn_34Gj_aIWd_ib_.n6ZYMtUsRx3R0t330mBNYunvmsm4J0TeaYq.EVHgn6AEd7CiG1KI9BrbWaJvhkJrAOjksngL0LSbhI74HqrbxBO5XIFWZiVTPUCuHWLRnysOGFGRWNaJh1p4nOWVRpz9XDpR; S_INFO=1676275738|0|##|2714837806@qq.com; P_INFO=2714837806@qq.com|1676275738|0|rms|00&99|jil&1676274347&rms#jil&220300#10#0#0|&0|rms|2714837806@qq.com; authUrsToken=auth:urs:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJFSFJfSVNTVUVSIiwiZXhwIjoxNjc4OTU0MTM4LCJpYXQiOjE2NzYyNzU3MzgsInVzZXJuYW1lIjoiMjcxNDgzNzgwNkBxcS5jb21AMTYzLmNvbSwxIn0.05tq8lwAL0fO2BiTcDmXr1wDm6BqyYKPukKkPO5MzEA; userName=; accountType=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'authority': 'hr.163.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,xh;q=0.7,ku;q=0.6',
    'authtype': 'ursAuth',
    'content-type': 'application/json;charset=UTF-8',
    'lang': 'zh',
    'origin': 'https://hr.163.com',
    'referer': 'https://hr.163.com/job-list.html?workType=1',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wyzp.middlewares.WyzpSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wyzp.middlewares.WyzpDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'wyzp.pipelines.WyzpPipeline': 300,
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
