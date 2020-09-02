
'''
问题背景： 处理大量不同类型的对象组成的复杂数据结构，每一个对象都需要进行不同的处理。
比如，遍历衣蛾树形结构，然后根据每个节点的响应状态执行不同的操作

刚开始的时候可能会写大量的if/else 语句来实现，访问者模式的好处就是通过getattr()来获取响应的方法，并利用递归遍历所有的节点

访问者模式一个缺点就是它严重依赖递归，如果数据结构嵌套层次太深可能会有
问题，有时候会超过 Python 的递归深度限制 (参考 sys.getrecursionlimit() )
'''


class HTTPHandler:

  def handle(self, request):
      methname = 'do_' + request.request_method
      getattr(self, methname)(request)


  def do_GET(self, request):
      pass


  def do_POST(self, request):
      pass


  def do_HEAD(self, request):
      pass
