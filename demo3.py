from urllib import parse,request
import os


post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

start_page = int(input('请输入起始页码:'))
end_page = int(input('请输入结束页码:'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

}
for page in range(start_page,end_page+1):
    # p = str(page)
    data = {
        'cname': '郑州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '5',
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(
        url = post_url,
        headers=headers,
        data=data,
    )
    response = request.urlopen(req)
    content = response.read().decode('utf-8')
    filename = 'data/{}.json'.format(page)
    with open(filename,'w',encoding='utf-8') as ftp:
        ftp.write(content)