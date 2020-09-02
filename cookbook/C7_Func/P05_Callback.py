from functools import wraps
from wrapt import decorator as wde
from decorator import decorator as de
'''


'''

#封装的一个函数，实现第一个函数执行完毕后将执行的结果传入到第二个函数中
#实现细节哟求去：在调用回调函数时，传的参数一定是第一个函数的return结果值
'''
编写回调函数： 内联回调函数。如第三方包wrapt这个包的装饰器，通过修饰函数，
 将被修饰装饰器函数的函数名、参数都能够收集到当前func的参数列表中。
 import wrapt
import  inspect

@wrapt.decorator
def logging(wrapped, instance, args, kwargs):  # instance is must
    print (wrapped.__name__)
    return wrapped(*args, **kwargs)

@logging
def say(something): pass

'''
def apply_async(func,args,*,callback):
      result=func(*args)
      callback(result)

def print_result(result):
      print('GOT:',result)


def add(x,y):
      return x+y

#callback 后面的函数不能够带括号。不带括号是变量赋值，最终由apply_async内部的callback参数去调用result去执行
#如果带了括号就是赋值，将右边函数的结果赋给callback.
r1=apply_async(add,(4,5),callback=print_result)
r1


'''
对回调函数进行扩展，增加下捕捉状态，需要在print_result函数上增加个类或者外函数。
 
  外函数处理额外加的参数，内函数还是来获取回调函数，以及处理额外的参数。最终还是在内函数内打印。
'''
def make_handle():
      sequemce=0
      def handleinner(result):
            nonlocal sequemce
            sequemce+=1
            print('[{}] GOT :{}' .format(sequemce,result))

      return  handleinner
handle=make_handle()

r2=apply_async(add,(4,5),callback=handle)
r2
r3=apply_async(add,('ni','hao'),callback=handle)

r3

'''
在对函数进行回调时，获取执行函数的return值后，放入回调函数中，默认是只能有return结果一个参数的

 如果需要额外的传参，就需要用到了冻结参数，将额外传参的值放入冻结参数内.
 
'''
from functools import partial

#当前类主要负责初始化一个实例，产生一个0开始的序列化
class SeqHadnle():
      def __init__(self):
            self.sequence=0

#这个函数利用产生的序列号放入自己参数列表内，和result结果，返回给回调函数
def class_result(result,seq):
            seq.sequence+=1
            print("[{}] GOT:{}".format(seq.sequence,result))

#初始化序列号类0
handle2=SeqHadnle()
                                                     #将调用的冻结函数，以及产生序列号的类实例0放在一块
r4=apply_async(add,('hello','world'),callback=partial(class_result,seq=handle2))
r4


#在这里可以使用lambda表达式，来接受上一个函数的执行结果。
#解析， 栏目大表达式中的r,代表原函数中执行的结果。即add函数和参数列表的执行结果。
r5=apply_async(add,('hello','world'),callback=lambda r:class_result(r,handle2))

#def apply_async(func,args,*,callback):
#      result=func(*args)
#      callback(result)


r5