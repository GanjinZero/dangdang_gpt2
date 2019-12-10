import os
import json
import requests


def grab_url(url, timeout=100):
    print(f"Grab url:{url}")
    url_head = 'http://localhost:8050/render.html?url='
    url_timeout = f"&timeout={timeout}"
    response = requests.get(url_head + url + url_timeout)
    print(f"Grab finish. Total length {round(len(response.text)/1024)}KB.")
    return response.text

def get_book_url_dict():
    book_information_file = "./book.txt"
    with open(book_information_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    book_url = dict()
    
    url_now = ""
    book_now = ""
    for line in lines:
        if line[0:4] == "http":
            url_now = line.strip()
            book_url[book_now] = url_now
        if line[0] != "¥" and line[0:4] != "http" and line.strip() != "":
            book_now = line.strip()

    print(f"Get url count:{len(book_url)}")
    return book_url

def main():
    book_url = get_book_url_dict()
    for book, url in book_url.items():
        result = grab_url(url, timeout=30)
        res = book + os.linesep + result
        if len(res) > 1000:
            file_name = "./data/" + url.split("/")[-1].split(".")[0] + ".txt"
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(res)

if __name__ == "__main__":
    main()

