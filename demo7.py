from urllib import parse, request
from lxml import etree

handler = request.ProxyHandler(
    proxies={
        'http': '183.163.40.223:31773'
    }
)
#  'http://www.mzitu.com/zipai/'
url = 'http://www.mmjpg.com'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.mmjpg.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
req = request.Request(url=url, headers=headers)
response = request.urlopen(req)

# opener = request.build_opener(handler)
# response = opener.open(req)
# content = response.read().decode('utf-8')

# src_path = '//div[@id="comments"]/ul/li//p/img/@src'
src_path = '//div[@class="pic"]//img/@src'
tree = etree.HTML(response.read().decode('utf-8'))
src_list = tree.xpath(src_path)
print(src_list)

i = 1
for p in src_list:
    # print(p)

    filename = 'data/{}.jpg'.format(str(i))
    request.urlretrieve(p, filename)
    print(filename + '保存成功')
    i += 1
