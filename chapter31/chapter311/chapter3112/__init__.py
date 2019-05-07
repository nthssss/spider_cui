# Request

"""
class Request:

    def __init__(
            self,
            url,   # 请求URL
            data=None,
                # 必须传bytes（字节流）类型；
                # 如果传字典，可以先用urllib.parse模块中的urlencode()编码。
            headers={},
                # 字典；
                # 可以在构造请求时通过headers参数直接构造，也可以通过调用请求实例的add_header()方法添加；
                # 最常用的用法是通过修改User-Agent来伪装浏览器（默认为Python-urllib）
                    # 火狐浏览器：Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
            origin_req_host=None,
                # 请求方的host名称或者IP地址
            unverifiable=False,
                # 表示这个请求是否是无法验证的，默认是False
                # 意思就是说用户没有足够权限来选择接收这个请求的结果。
                    # 例如，我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，这时unverifiable的值就是True`。
            method=None
                # 字符串，用来指示请求使用的方法，比如GET、POST和PUT等
    ):
"""