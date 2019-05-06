import urllib.request
from pprint import pprint
response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))  # 网页源代码
# print(type(response))  # 响应属性
print(response.status)  # 相应状态码
pprint(response.getheaders())  # 响应头
pprint(response.getheader('Server'))  # 响应头中Server的值

# def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#             *, cafile=None, capath=None, cadefault=False, context=None):