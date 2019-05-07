# 高级用法
# Handler
# BaseHandler
# urllib.request模块里的BaseHandler类，它是所有其他Handler的父类，它提供了最基本的方法，例如default_open()、protocol_request()等。
# HTTPDefaultErrorHandler：用于处理HTTP响应错误，错误都会抛出HTTPError类型的异常。
# HTTPRedirectHandler：用于处理重定向。
# HTTPCookieProcessor：用于处理Cookies。
# ProxyHandler：用于设置代理，默认代理为空。
# HTTPPasswordMgr：用于管理密码，它维护了用户名和密码的表。
# HTTPBasicAuthHandler：用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题。
# Opener
# OpenerDirector
# 我们可以称为Opener。我们之前用过urlopen()这个方法，实际上它就是urllib为我们提供的一个Opener。
# 之前使用的Request和urlopen()相当于类库为你封装好了极其常用的请求方法，利用它们可以完成基本的请求，
# 但是现在不一样了，我们需要实现更高级的功能，所以需要深入一层进行配置，使用更底层的实例来完成操作，所以这里就用到了Opener。
# Opener可以使用open()方法，返回的类型和urlopen()如出一辙。
#
# 利用Handler来构建Opener。
