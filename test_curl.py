import os
import subprocess


def curl(url):
    a = subprocess.Popen(f'curl {url}').decode("gb2312").read()
    return a

curl("http://product.dangdang.com/27932914.html")
