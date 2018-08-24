from urllib import request

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

}

req = request.Request(url=url,headers=headers)

# response = request.urlopen(req)

handler = request.HTTPHandler()
opener = request.build_opener(handler)
response = opener.open(req)
content = response.read().decode('utf-8')


with open('data/du.html','w',encoding='utf-8') as ftp:
    ftp.write(content)

