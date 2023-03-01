# Scrapy settings for anjke project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'anjke'

SPIDER_MODULES = ['anjke.spiders']
NEWSPIDER_MODULE = 'anjke.spiders'

MEDIA_ALLOW_REDIRECTS =True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'anjke (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

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
  # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie': 'focus_wsid=flxxjw3p23-4lh701-bhw330-9nc4-tilex97wkn75; focus_waf_token=ad6d280c64f1206a1643e964b15dd54e; gr_user_id=00482a36-3886-46ad-84de-3fb82666c7da; __bid_n=18603190cf17fbffe54207; FPTOKEN=0krMyn4POU5PpMVRXPLLR3tgNNyWd5GfZg+XaDCZaeJTDJuciIFJ5vVYS07yeP4O9kX7Qb+ppwWk3ABwwXb+vF85yrycF/mIH53sMWh54mbrqkNFkSBqMtOUizwRbDdAqGqKhUxqDSfu6n5z3j1y4reuSgHwcOJfL7chOitm0zvUb2Rzs4RQT6nD6MwkGNP+3J5BlBxYMc4FoXMV3EuvC0UVNdC6XQpXaE+Fxi0AOEG6Jj5aXrV5KAVQYHARwjcMl8/Sb18qiMOGHGb2OEIiaugO+UFtAhNE/bLKpfLmksg2PR+iJYsTnFNpcCsGFhPe4gkxkHC6Fqxz9pEFRSGNNQ0hqJQe/vlOlMnhFwE5GStgyhlp9lY8CeX3KuhbTGAU0HcqdqQ6MUJlGXgxhLrFEt8y1O0i9h0iEZkkqSvLVXr97+SQuNGhBHZnJY4EbE2Z|7lotpxrgdT6P5l9gs5+6yxnKLFw9ThEzYrwdbbb5hdI=|10|8bd64a0c093061179b48f6791518bef0; wap_ad_loupan=0; focus_pc_city_p=sh; focus_city_p=sh; focus_city_c=310100; focus_city_s=sh; 87a4bcbf0b1ea517_gr_session_id=0b011a57-889c-409b-a0cd-807481f187a1; 87a4bcbf0b1ea517_gr_session_id_0b011a57-889c-409b-a0cd-807481f187a1=true; focus_mes_info=direct%40%40%40%40%40%40%40%40%40%40%40%40%40%40%40%40%40%40null%40%40null%40%40null%40%40'
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'anjke.middlewares.AnjkeSpiderMiddleware': 543,
#}
LOG_LEVEL = 'WARNING'
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'anjke.middlewares.AnjkeDownloaderMiddleware': 543,
   # 'anjke.middlewares.UserAgentMiddleware': 543,
   # 'anjke.middlewares.ChangeIPMideeleware': 542,
   # 'anjke.middlewares.ChangeUAMideeleware': 541,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'anjke.pipelines.AnjkePipeline': 300,
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
