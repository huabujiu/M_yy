import requests
from bs4 import BeautifulSoup

sessions = requests.Session()
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
s = sessions.get(url=url,headers=headers)



soup = BeautifulSoup(s.text,'lxml')
view_state = soup.select('#__VIEWSTATE')[0].attrs['value']
view_states = soup.select('#__VIEWSTATEGENERATOR')[0].attrs['value']
base_url = soup.select('#imgCode')[0].attrs['src']
img_url = 'https://so.gushiwen.org' + base_url

img = sessions.get(url=img_url)
with open('data/{}.jpg'.format(base_url),'wb') as fp:
    fp.write(img.content)
code = input('请输入验证码:')

data = {
    '__VIEWSTATE':view_state,
    '__VIEWSTATEGENERATOR':view_states,
    'from':'https://so.gushiwen.org/user/collect.aspx',
    'email':'1271537971@qq.com',
    'pwd':'1271537971',
    'code':code,
    'denglu':'登录',
}
con = sessions.post(url=url,headers=headers,data=data)
with open('data/gs.html','wb') as fp:
    fp.write(con.content)