from urllib import parse
from urllib import request
import re

url = 'http://www.baidu.com'

# response = request.urlopen(url)
# content = response.read().decode('utf-8')
#
# with open('data/baidu.html','w',encoding='utf-8') as ftp:
#     ftp.write(content)

# request.urlretrieve(url,'data/bd.html')


# img_url = 'http://img4.imgtn.bdimg.com/it/u=2813434517,83142011&fm=200&gp=0.jpg'
# request.urlretrieve(img_url,'data/girl.jpg')

video_url = 'https://v.qq.com/x/page/q0384r9kdz5.html'
response = request.urlopen(video_url)
content = response.read().decode('utf-8')
r = r"href='(http.*\.mp4)"
re_mp4 = re.compile(r)
mp4list = re.findall(re_mp4,content)
filename=1
for mp4url in mp4list:
    request.urlretrieve(mp4url,'%s.mp4' %filename)
    print('"%s.mp4" ok' %filename)
    filename += 1

# with open('data/v.mp4','wb') as ftp:
#     ftp.write(content)


