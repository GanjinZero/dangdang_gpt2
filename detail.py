import json
import re
import requests
from requests import RequestException


def get_one_page(url):
    try:
        opt = os.popen(f"curl {url}")
        return opt.read()
    except BaseException:
        return None

def parse_one_page(html):
    #  加上re.S后, .将会匹配换行符
    pattern = re.compile('<li>.*?list_num.*?>(.*?)</div>.*?pic.*?src="(.*?)".*?/></a>.*?name"><a.*?title="(.*?)">.*?tuijian">(.*?)</span>.*?publisher_info.*?title="(.*?)".*?biaosheng.*?<span>(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'iamge':item[1],
            'title':item[2],
            'tuijian':item[3],
            'author':item[4],
            'times':item[5],
        }

def write_content_to_file(content):
    with open('book_detail.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(url):
    html = get_one_page(url)
    print(html)
    if html:
        print(html)
        parse_result = parse_one_page(html)
        for item in parse_result:
            print(item)
            write_content_to_file(item)

if __name__ == "__main__":
    main('http://product.dangdang.com/25119332.html')
