from urllib import request
import re
import time
import os



# <div class="thumb">
# 	<a href="/article/120719293" target="_blank">
# 		<img src="//pic.qiushibaike.com/system/pictures/12071/120719293/medium/app120719293.jpeg" alt="哈哈哈哈哈">
# 	</a>
# </div>

def get_img(url, page):
    img_url = url + str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    req = request.Request(url=url, headers=headers)
    return req


# print(content)




def down_img(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    img_srcs = pattern.findall(content)
    for img_src in img_srcs:
        # print(img_src)
        img_url = 'https:' + img_src
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename = img_url.split('/')[-1]
        filepath = dirname + '/' + filename
        print('开始打印图片%s' %filename)
        request.urlretrieve(img_url, filepath)
        print('打印图片%s结束' %filename)
        time.sleep(2)

# for img_src in img_srcs:
# 	print(img_src)

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        req = get_img(url, page)
        response = request.urlopen(req)
        content = response.read().decode('utf-8')
        print('开始打印%s页图片' %page)
        down_img(content)
        print('结束打印%s页图片' % page)
        time.sleep(3)



if __name__ == '__main__':
    main()
