import requests
import execjs

with open('.\encode.js','r',encoding='utf-8') as f:
    encode_js = execjs.compile(f.read())

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'UM_distinctid=16f20f62ad2800-0e8dcdbd722dc7-2393f61-1fa400-16f20f62ad3336; CNZZDATA1277593802=78969491-1576805718-%7C1577349168',
'Host': 'tool.liumingye.cn',
'Origin': 'http://tool.liumingye.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}

formdata = {
    'data':encode_js.call('encode',"text=突然的自我&page=1&type=migu")
}

resp = requests.post('http://tool.liumingye.cn/music/ajax/search',headers=headers,data=formdata)
print(resp.json())