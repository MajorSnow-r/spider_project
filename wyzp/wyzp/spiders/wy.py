import scrapy
import json
from wyzp.items import WyzpItem


class WySpider(scrapy.Spider):
    name = 'wy'
    allowed_domains = ['hr.163.com']
    start_urls = ['https://hr.163.com/api/hr163/position/queryPage']

    def start_requests(self):
        for j in range(1, 280):
            yield scrapy.Request(url='https://hr.163.com/api/hr163/position/queryPage',
                                 callback=self.parse,

                                 method='POST',
                                 # 请求头用于告诉服务器请求的数据格式是json的,通过Content-type来告诉服务器请求的数据格式是json的
                                 headers={
                                     'Content-Type': 'application/json'
                                 },
                                 # 直接携带json数据,不用携带表单了
                                 # dumps的意思就是将字典转成字符串
                                 body=json.dumps({
                                     "currentPage": j,
                                     "pageSize": 10,

                                 }),
                                 )

    def parse(self, respons, **kwargs):
        json_data = respons.text
        dic = json.loads(json_data)
        for i in dic['data']['list']:
            items = WyzpItem()
            items['title'] = i['name']
            items['bumen'] = i["firstDepName"]
            items['zhice'] = i['firstPostTypeName']
            items['xli'] = i['reqEducationName']
            items['rshu'] = i['recruitNum']
            items['dizhi'] = i['workPlaceNameList']
            items['jingyan'] = i['reqWorkYearsName']
            items['ganw_miaoshu'] = i['description']
            items['gangw_zhize'] = i['requirement']
            print(items)
            yield items
