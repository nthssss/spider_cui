import requests

headers = {
    'Cookie': """_xsrf=r6VlXCaNgOPQEmY1Q3SjvjfPlChOWnFg; _zap=d284cd99-02bf-40dc-8599-164e4cc3d506; d_c0="AJBjnEzp6A6PTkShFveUVHe9EtcqH-v21KE=|1548928583"; z_c0=Mi4xdzg5ekFBQUFBQUFBa0dPY1RPbm9EaGNBQUFCaEFsVk5YaFJBWFFCdmdxaFNUSWNKRlNvS3Vhd0Rhdzl1czQ1LXVR|1548928606|9c0a22ccda85c2ee76c0df45e3e15d2e08bce65e; __gads=ID=f40f2c3d513b495f:T=1554822555:S=ALNI_Mb-QSsaZRRTWUxDlGwKe1WTF77v7g; q_c1=4abe27f758574799b45fa42a3378b70b|1556821674000|1548928610000; __utmz=51854390.1557330783.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20140817=1^3=entry_date=20140817=1; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c; __utma=51854390.859412777.1557330783.1557330783.1558176482.2; __utmb=51854390.0.10.1558176482; __utmc=51854390""",
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
from pprint import pprint
pprint(r.text)