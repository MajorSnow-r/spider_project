import requests
import execjs
yh_inp = input('请输入要翻译的内容:')
cookies = {
    '__bid_n': '185b9a4af45d3f8f5a4207',
    'BIDUPSID': 'FFDF9FC8221F8CA31D2B7B811062D59F',
    'PSTM': '1674000561',
    'BAIDUID': '51C75E2E9BAD7807981105DBA7EFAA5D:FG=1',
    'ZFY': '5xt5oJ5fV5zvZgTZl8VOYFZ3nAkKTd1BLUYut:ApNwzc:C',
    'newlogin': '1',
    'WP_EE_OFFICE_TOKEN': '2074553514_121.810bd6f7e4ea57f10e5dc8898f9939e5.YB7tRD2lF6JxT5Gl3tjNE_whX60L3KjVN_TdF3Y.KRkPLw',
    'BAIDUID_BFESS': '51C75E2E9BAD7807981105DBA7EFAA5D:FG=1',
    'BDUSS_BFESS': 'JXRDhXb2NVaDJmU1RTaHdtUXBIMmlCTVZHUFdmSTVYVHFZZWd1R1hOVzBRaDVrRUFBQUFBJCQAAAAAAAAAAAEAAABie3WjbWFudG91YmFiYV8xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALS19mO0tfZjeX',
    'BDRCVFR[F_eszSxO873]': 'mk3SLVN4HKm',
    'H_PS_PSSID': '26350',
    'ZD_ENTRY': 'bing',
    'FPTOKEN': '8+x2vN7rBEQTe0TjvHU7t4QJQstqIU0MDP43pKCWe0SepSoha8MxRZ+SaceyDfugXAaA6iudhf15olUmNmOH/4dfcGxHeZ5/Xna2lt22ahyeJotI9xHS5/2UeoqfaFQoHN2O7bIQZCakFOSVkQkGNzoMmwRpDLetspMBX75c6f5YOpij73Y+qEOJvNTd5Zem8DsWSbW4iNITV6MIBw4NeIddliL0skOraPnPCgQE1wMvHHyQmWW8meT4lD5ACFQn28JjQiFEo5nfk0r/Pu0RJ4oCw4BP5WGmdeouLvSJp0JM6aqqTSnEtkNEdyJFQypA/jBCjMCPSgyKBgRAhRbKa5Uc818ECvGMUDrX1JMG0oWGp/Lsjbl8h1n8z3XCN90utnXLLNz1hxpGS0RKzsG1cw==|fsoWiMQbL2fPi6KzSK+82WhH/5PGnpmdBcI8XjLHp7k=|10|8a1a39766a25e2662af12ad026144310',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1677842064',
    'APPGUIDE_10_0_2': '1',
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'ab_sr': '1.0.1_MWY4Njc4NmNlMjA5NDM5MjlkMzM3YzRkNWMzMTUxZDYxMjEyMWZiZWJkZjc0NmJkODVmY2FhZDc4MDZiMzQ0MWZhMDc4ZDI4Y2U0NTJkNmEwZGEzNjhmNDMwYWQ0MGM1NzUzODI2NWIyNDUzNzZiNmRhMTIwZGNlMTE5OTJkYzFjZWQ5ZTJkMTc0YTlhY2U5YzU3N2E0OTA4MWM3ZmQ1ZDI3MjY4ODMxN2UwYTFhZTE1MzNmOTZhMjZjMDA3MzRi',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1677845808',
}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,xh;q=0.7,ku;q=0.6',
    'Acs-Token': '1677845810904_1677845933212_OyIckPG4eEOHT2YhKXSMLtj9p30FC4tucB+ja1w/oN2FzzxObr1NdqnQWkp5lEg8DQvLpKHNR8PvmZn0Gq9KPnOg3h/PLOSm3FsYbLCjOQc/AYDHfH3jPRvTaPp/af6ABU2bXQ+CZ0H/JugLyjVLAW+KLDrgMe8qtKEq+9SCpI639xfq6jffxbY+HL2MRkIjJubvF5nuhhAZt2shhA1F5KOl3LTw1Gpj7t2OpzBKsWcGqKwF0rXsZHPLRzyrs5zBZyopjaOufmVzuWWXEv1SSQfVXJSVmGbFw+VkEw6DJhExMXq37uqQA+tpmZ8Ms8glNL5cHRtjo+NRywFG6/6mXFPDLhhgPZa6f/mae2O+090=',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '__bid_n=185b9a4af45d3f8f5a4207; BIDUPSID=FFDF9FC8221F8CA31D2B7B811062D59F; PSTM=1674000561; BAIDUID=51C75E2E9BAD7807981105DBA7EFAA5D:FG=1; ZFY=5xt5oJ5fV5zvZgTZl8VOYFZ3nAkKTd1BLUYut:ApNwzc:C; newlogin=1; WP_EE_OFFICE_TOKEN=2074553514_121.810bd6f7e4ea57f10e5dc8898f9939e5.YB7tRD2lF6JxT5Gl3tjNE_whX60L3KjVN_TdF3Y.KRkPLw; BAIDUID_BFESS=51C75E2E9BAD7807981105DBA7EFAA5D:FG=1; BDUSS_BFESS=JXRDhXb2NVaDJmU1RTaHdtUXBIMmlCTVZHUFdmSTVYVHFZZWd1R1hOVzBRaDVrRUFBQUFBJCQAAAAAAAAAAAEAAABie3WjbWFudG91YmFiYV8xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALS19mO0tfZjeX; BDRCVFR[F_eszSxO873]=mk3SLVN4HKm; H_PS_PSSID=26350; ZD_ENTRY=bing; FPTOKEN=8+x2vN7rBEQTe0TjvHU7t4QJQstqIU0MDP43pKCWe0SepSoha8MxRZ+SaceyDfugXAaA6iudhf15olUmNmOH/4dfcGxHeZ5/Xna2lt22ahyeJotI9xHS5/2UeoqfaFQoHN2O7bIQZCakFOSVkQkGNzoMmwRpDLetspMBX75c6f5YOpij73Y+qEOJvNTd5Zem8DsWSbW4iNITV6MIBw4NeIddliL0skOraPnPCgQE1wMvHHyQmWW8meT4lD5ACFQn28JjQiFEo5nfk0r/Pu0RJ4oCw4BP5WGmdeouLvSJp0JM6aqqTSnEtkNEdyJFQypA/jBCjMCPSgyKBgRAhRbKa5Uc818ECvGMUDrX1JMG0oWGp/Lsjbl8h1n8z3XCN90utnXLLNz1hxpGS0RKzsG1cw==|fsoWiMQbL2fPi6KzSK+82WhH/5PGnpmdBcI8XjLHp7k=|10|8a1a39766a25e2662af12ad026144310; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677842064; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MWY4Njc4NmNlMjA5NDM5MjlkMzM3YzRkNWMzMTUxZDYxMjEyMWZiZWJkZjc0NmJkODVmY2FhZDc4MDZiMzQ0MWZhMDc4ZDI4Y2U0NTJkNmEwZGEzNjhmNDMwYWQ0MGM1NzUzODI2NWIyNDUzNzZiNmRhMTIwZGNlMTE5OTJkYzFjZWQ5ZTJkMTc0YTlhY2U5YzU3N2E0OTA4MWM3ZmQ1ZDI3MjY4ODMxN2UwYTFhZTE1MzNmOTZhMjZjMDA3MzRi; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1677845808',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = {
    'from': 'zh',
    'to': 'en',
}
"""
    打开调试的js文件
    切记路径不要写错
"""
with open("D:\py\JS逆向\百度翻译.js",encoding="utf-8")as f:
    js_code = f.read()
"""编译js代码"""
comp = execjs.compile(js_code)
"""
    调用js代码
    第一个参数是js函数名称
    第二个参数是需要翻译的内容
"""
resu = comp.call('xsr',yh_inp)
print(resu)
data = {
    'from': 'zh',
    'to': 'en',
    'query': yh_inp,
    'simple_means_flag': '3',
    'sign': resu,
    'token': '312fe0fa48bb7a151e67d03c15799283',
    'domain': 'common',
}
response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers, data=data)

jsoo = response.json()
dic_text = jsoo['trans_result']['data']
for i in dic_text:
    print(i['dst'])