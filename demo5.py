from urllib import parse, request
from urllib.error import URLError, HTTPError
import os


def creat_req(braname,page,url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    data = {
        'kw':braname,
        'pn':page,
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url=url,headers=headers,data=data)

    return req

def create_response(req):
    return request.urlopen(req)

def create_content(response):
    return response.read().decode('utf-8')

def save_data(filapath,filaname,content):
    file = os.path.join(filapath,filaname)
    try:
        with open(file,'w',encoding='utf-8') as ftp:
            ftp.write(content)

    except HTTPError as e:
        print('HTTPError')
        print(e)

    except URLError as e:
        print('URLError')
        print(e)

    except Exception as e:
        print('未知错误')

    else:
        print('ojbk')

if __name__ == '__main__':
    braname = input('请输入字符串:')
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    url = 'https://tieba.baidu.com/'
    for page in range(start_page,end_page+1):
        req = creat_req(braname,page,url)
        response = create_response(req)
        content = create_content(response)
        filepath = 'data/'
        filename = '{}.html'.format(page)
        save_data(filepath,filename,content)

