import requests
url_register = "http://127.0.0.1:8000/api/v1/user/register/"
url_querr = "http://127.0.0.1:8000/api/v1/user/querr/"
url_login = "http://127.0.0.1:8000/api/v1/user/login/"
url_article = "http://127.0.0.1:8000/api/v1/user/article/"
url_articlelist = "http://127.0.0.1:8000/api/v1/user/articlelist/"
res = requests.post(url_articlelist).json()
print(res)