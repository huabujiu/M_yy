from urllib import parse,request
from lxml import etree

list = etree.parse('data/test.html')

print(list.xpath('//div[@class="gushi"]/ul/li/text()'))