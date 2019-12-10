import re
from html import unescape
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import json


def html_to_text(html_file):
    with open(html_file, 'r', encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "lxml")
    text = soup.find_all(id="detail")
    pat = re.compile('>(.*?)<')
    result = ""
    for t in text:
        x = ' '.join(pat.findall(str(t)))
        x = x.replace("&lt;br", " ")
        x = x.replace("/&gt;", " ")
        result += x + " "
    
    return result
    
for root, dirs, files in os.walk("./data/"):
    all_text = []
    for f in tqdm(files):
        f_n = os.path.join(root, f)
        text = html_to_text(f_n)
        all_text.append(text)
    with open("./train.json", "w", encoding="utf-8") as f:
        json.dump(all_text, f)

