import json
import requests
import csv


class zhaotoubiao():

    def __init__(self):
        self.li = []
        with open(file="金昌市招投标信息.csv", mode="w", encoding='utf-8', newline="") as f:
            fils = csv.DictWriter(f,
                                  fieldnames=['content', 'informationType', 'releaseTime', 'projectId', 'projectName',
                                              'projectNo', 'tradingNo', 'tenderOrganizationFormDictLable', 'tenderer',
                                              'agencyName', 'bidWay', 'qualification', 'jdCompany',
                                              'bidContentScope', 'name', 'openBidTime', 'tenderContent',
                                              'otherBidContent',
                                              'bidderRequirements'])
            fils.writeheader()

    """列表页"""

    def send(self):
        headers = {
            'Cookie': 'ASP.NET_SessionId=qi4dxett5zxy0x13v2e0gvyq; SESSION=b0ef168e-19a6-4cec-ac80-9df0b598b36b',
            'Referer': 'https://ggzy.jcs.gov.cn/website/transaction/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        }
        for i in range(1, 7):
            params = {
                'pageNum': i,
                'pageSize': 20,
                'informationType': 'ANNOUNCEMENT',
                'projectType': 'SZFJ',
                'informationName': 'ZBGG',
            }
            response = requests.get(
                'https://ggzy.jcs.gov.cn/pro-api-construction/construction/bidder/bidSection/list',
                params=params,
                headers=headers,
            )
            """解析首页数据"""
            dict_json = json.loads(response.text)
            rows = dict_json['rows']
            for i in rows:
                """保存要获取的数据"""
                dict = {}
                """保存详情页翻页数字"""
                dicts = {}
                dict['content'] = i['content']
                dict['informationType'] = i['informationType']
                dict['releaseTime'] = i['releaseTime']
                dicts['projectId'] = i['projectId']
                self.xiang_send(dict, dicts)

    """详情页"""

    def xiang_send(self, dict, dicts):
        xiang_text = requests.get(
            url='https://ggzy.jcs.gov.cn/pro-api/web/tradingInfo/getConstructionProjectInfo/{}'.format(
                dicts['projectId']))
        """解析详情页"""
        json_dict = json.loads(xiang_text.text)
        dates = json_dict['data']
        dict['projectName'] = dates['projectName']
        dict['projectNo'] = dates['projectNo']
        dict['tradingNo'] = dates['tradingNo']
        try:
            dict['tenderOrganizationFormDictLable'] = dates['tenderOrganizationFormDictLable']
        except:
            dict['tenderOrganizationFormDictLable'] = "空"
        dict['tenderer'] = dates['tenderer']
        dict['agencyName'] = dates['agencyName']
        dict['bidWay'] = dates['bidWay']
        try:
            dict['qualification'] = dates['qualification']
        except:
            dict['qualification'] = "空"
        try:
            dict['jdCompany'] = dates['jdCompany']
        except:
            dict['jdCompany'] = "空"
        dict['bidContentScope'] = dates['bidContentScope']
        """tradingBidSectionVOS-列表"""
        tradingBidSectionVOS = dates['tradingBidSectionVOS']
        for ding in tradingBidSectionVOS:
            dictss = {'name': ding['name'], 'openBidTime': ding['openBidTime'], 'tenderContent': ding['tenderContent'],
                      'otherBidContent': ding['otherBidContent'], 'bidderRequirements': ding['bidderRequirements']}
            dict.update(dictss)
        self.baocun(dict)

    """保存数据"""

    def baocun(self, dict):
        li_word = [dict]
        for word in li_word:
            with open(file="金昌市招投标信息.csv", mode="a", encoding='utf-8', newline="") as f:
                fils = csv.DictWriter(f, fieldnames=['content', 'informationType', 'releaseTime', 'projectId',
                                                     'projectName', 'projectNo', 'tradingNo',
                                                     'tenderOrganizationFormDictLable', 'tenderer', 'agencyName',
                                                     'bidWay', 'qualification', 'jdCompany',
                                                     'bidContentScope', 'name', 'openBidTime', 'tenderContent',
                                                     'otherBidContent',
                                                     'bidderRequirements'])
                fils.writerow(word)


if __name__ == '__main__':
    diao = zhaotoubiao()
    diao.send()
