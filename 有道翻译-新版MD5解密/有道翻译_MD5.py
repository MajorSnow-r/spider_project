import re
from time import time
import requests
from hashlib import md5
import base64
from Crypto.Cipher import AES


# 密文解密
def AES_jiemi(mi_text):
    key = b'\x08\x14\x9d\xa7\x3c\x59\xce\x62\x55\x5b\x01\xe9\x2f\x34\xe8\x38'
    iv = b'\xd2\xbb\x1b\xfd\xe8\x3b\x38\xc3\x64\x36\x63\x57\xb7\x9c\xae\x1c'
    """创建AES对象,传入对应方法cbc"""
    aes = AES.new(key, AES.MODE_CBC, iv)
    """decrypt解密base64位"""
    ctx = aes.decrypt(base64.urlsafe_b64decode(mi_text))
    """指定编码"""
    xxx = ctx.decode("UTF-8").strip()
    return xxx


# MD5加密,获取加密数据
def MD5_jiami():
    """时间戳"""
    d_time = int(time() * 1000)
    enx = f"client=fanyideskweb&mysticTime={d_time}&product=webfanyi&key=fsdsogkndfokasodnaso"
    """实例化一个MD5加密对象"""
    obj = md5()
    """将明文转成加密后的数据,并且指定编码"""
    obj.update(enx.encode("utf-8"))
    """将加密的结果转成16进制"""
    sing = obj.hexdigest()
    """返回解密后的结果"""
    return sing


def request_yd(key, mi):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,xh;q=0.7,ku;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1930297505@10.110.96.160; OUTFOX_SEARCH_USER_ID_NCOO=1509930523.2108824',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'i': key,
        'from': 'auto',
        'to': '',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': mi,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': int(time() * 1000),
        'keyfrom': 'fanyi.web',
    }
    response = requests.post('https://dict.youdao.com/webtranslate', headers=headers, data=data)
    return response.text


if __name__ == '__main__':
    while True:
        key = input("请输入内容:")
        mi = MD5_jiami()
        mi_text = request_yd(key, mi)
        zhu = AES_jiemi(mi_text)
        """处理乱码问题"""
        pattern = re.compile('[\x00-\x08\x0b-\x0c\x0e-\x1f\ ]')
        zhu = pattern.sub('', zhu)
        # print(zhu)
        te = re.search('"#text":"(.*?)"', zhu).group()
        print(te)
