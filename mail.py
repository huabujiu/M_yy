from urllib import request, parse
from http.cookiejar import CookieJar

post_url = 'https://mail.163.com/js6/main.jsp?sid=SCvYoOwrduQXzdIlSArrBKYxVTrtGJBw&df=mail163_letter#module=welcome.WelcomeModule|{}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
cookie = CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
data = {
   #配置自己的账号信息
    "un":  "15713816983@163.com",
pkid	CvViHzl
pd	mail163
rtid	C2xWitJioYQ2AUCIswUYWcp8vN9eFH0Q
topURL	https://mail.163.com/
nocache	1531881319580
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
