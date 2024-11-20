import requests

# url = "https://api.github.com/search/repositories"
#
# params = {"q": "language:html"}
#
# response = requests.get(url, params=params)
#
# print(f"Status code: {response.status_code}")
# print(response.json())








import requests

# url = "https://jsonplaceholder.typicode.com/posts"
#
# params = {
#     'userId' : 1
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     posts = response.json()
#     for post in posts:
#         print(post)
# else:
#     print("Error")









url = "https://jsonplaceholder.typicode.com/posts"

data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, json=data)

print(f"Status code: {response.status_code}")
print(f"ответ - {response.json}")