import requests


url_head = 'http://localhost:8050/render.html?url='

url_test = 'http://product.dangdang.com/26921715.html'

wait_time = 100
url_wait = f"&timeout={wait_time}"

response = requests.get(url_head + url_test + url_wait)
print(response.text)
