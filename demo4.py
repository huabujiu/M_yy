from urllib import request
from urllib.error import HTTPError,URLError

url = 'http://www.shabi.com'

# req = request.Request(url)

try:
    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    print('shabi')
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