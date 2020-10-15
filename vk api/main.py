import vk_api
import requests

## DiMa2000contractwars@yandex.ua A toLower is bad
#tokenData = 'ab9d5dd4b50b79489154286f624d0d66b36f1ad760374d3028e906368109f41893944a2e3e89b1a7284f97'
#token = vk_api.VkApi(token=tokenData, session=s)
#vk = token.get_api()

print(vk_api.__version__)

## http://free-proxy.cz/ru/proxylist/country/all/https/ping/all
proxies = {
    'https': 'https://51.161.116.223:3128'
}

s = requests.Session()
s.proxies.update(proxies)

vk_session = vk_api.VkApi('номер', 'пароль', session=s)
vk_session.auth()

vk = vk_session.get_api()

# ## Удаляются в обратном порядки примерно по 3 поста в секунду
# posts = vk.wall.get(count=100)['items']
#     while(posts):
#         for post in posts:
#             print(post['id'])
#             vk.wall.delete(post_id=post['id'])
#         posts = vk.wall.get(count=100)['items']

response = vk.wall.post(message='ломаю попу ельца')
print(response)

# link = "https://api.vk.com/method/users.get?user_id=210700286&v=5.52"
# #link = "https://httpbin.org/get"

# response = requests.get(link, proxies = proxies)
# #response.raise_for_status()
# jsonResponce = response.json()
# print(jsonResponce)