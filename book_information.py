import requests
from lxml import html

name = input('请输入要搜索的图书信息:')
# 1.准备url
url = 'http://search.dangdang.com/?key={}&act=input'.format(name)
start = 1
while True:
    print('正爬取第' + str(start) + '页信息')
    start += 1
    # 2.发送请求获取数据
    response = requests.get(url)

    # 3.获取html字符串
    strs = response.text

    # 4.获取element对象
    element = html.fromstring(strs)

    # 5.先获取分类
    li_list = element.xpath('//div[@id="search_nature_rg"]/ul/li')

    # 6.再获取数据
    for li in li_list:
        book_name = li.xpath("./a/@title")[0]
        book_link = li.xpath("./a/@href")[0]
        book_price = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')
        if not book_price:
            book_price = li.xpath('./div[@class="ebook_buy"]/p[@class="price e_price"]//text()')
        if not book_price:
            book_price = ['没有价格']
        with open('book.txt', 'a', encoding='utf8') as f:
            f.write(book_name.strip() + "\n" + book_link + "\n" + book_price[0] + "\n\n")
    try:
        # 爬取下一页
        a_url = element.xpath('//li[@class="next"]/a/@href')[0]
        url = 'http://search.dangdang.com' + a_url
    except:
        print('完成，共爬取了' + str(start - 1) + '页,请在book.txt中查看')
        break
