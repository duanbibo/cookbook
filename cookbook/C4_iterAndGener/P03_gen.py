

def gen(x):
     '''这里生成器必须用while循环一直处理，生成器不需要捕捉stopiter异常'''
     while x>0:
           yield x
           x-=1
g=gen(8)
print(g)
for i in g:
      print(i)


''' 试一下 yield from语句  
 yield  from语句本身其实是个委托生成器
from后面也是个子生成器函数 ，实际工作的内容 '''

iters=[[1,2],[2,3],[3,4],[4,5],[5,5]]

def yfrom(parm):
      #这个for循环解析的为最外层的多个可迭代对象，i为每个可迭代对象的实例
      for i in  parm:
            #这里自动解析最内层的每一个可迭代对象
            yield from i


c=yfrom(iters)
print(c)
for i in c:
      print(i,end='..')

'''
 编写个 委派生成器、子生成器的demo
'''