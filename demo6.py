from urllib import request, parse
from http.cookiejar import CookieJar

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201842926368'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
cookie = CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
data = {
   #配置自己的账号信息
    "email":"dqsygcz@126.com",
	"origURL":"http://www.renren.com/home",
	"domain":"renren.com",
	"key_id":"1",
	"captcha_type":"web_login",
	"password":"bc95dbb4e9cfbd8f3b84e6cd1820d210bf6953f4d70630f73a750369c166e61d",
	"rkey":"932a8efd469514758b8787a3631dd539",
}
data = parse.urlencode(data).encode('utf-8')
response = request.Request(url=post_url,headers=headers,data=data)
opener.open(response)

url = 'http://www.renren.com/224549540/profile'
req = request.Request(url=url,headers=headers)
response = opener.open(req)
content = response.read().decode('utf-8')

with open('data/rr.html','w',encoding='utf-8') as ftp:
    ftp.write(content)
