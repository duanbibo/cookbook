import time
from functools import wraps

'''
编写装饰器，带参数的装饰器，不带参数的装饰器


    装饰器其实是一个内联调用函数，在内部执行func(*args,**kwargs)
    使用wraps的目的是为了不修改原始函数的参数签名以及返回值；
    使用不定长参数的目的是确保任何参数都能够收集处理。
    
    
    
'''


def timethis(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
            start = time.time()

            result = func(*args, **kwargs)  # 核心是这一块
            end = time.time()
            print(func.__name__, end - start)

            return result  # 最终返回执行结果

      return wrapper

#最优雅的写法
@timethis
def countdown(n):
      while n>0:
            n-=1

countdown(8999999)

#第二种写法，不改变原函数的基础上，使用原函数为参数。返回装饰后的方法    funcRestlt=decprator(x,y,z)(func)
def countdown2(n):
      while n>0:
            n-=1
method=timethis(countdown2)
method(8999999)

'''
解除装饰器函数 :
  
  通过被装饰器修饰的函数名，调用 __wrapped__ 魔法函数进行取消装饰
  
'''
@timethis
def add(x,y):
      return x+y

orig_count=add.__wrapped__
print(orig_count(3,4))

'''
定义带参数的装饰器 ：  外层处理装饰器的参数， 中间处理被修饰的函数，内部用wraps修饰函数，在做调用。
wraps 永远用在最内层


#装饰器带参数的语法糖：     func=decorator(x,y,z)(func)
'''
import logging


def loged(level, name=None, message=None):


      def decorate(func):

            #在这一层的内部，处理、解析装饰器的函数。如果与被修饰的函数有关联的话，可以推迟到这里面
            logname = name if name else func.__module__
            log = logging.getLogger(logname)
            logsmg = message if message else func.__name__

            @wraps(func)
            def wrapper(*args, **kwargs):
                  log.log(level, logsmg)
                  return func(*args, **kwargs)

            return wrapper

      return decorate

@loged(logging.DEBUG)
def add2(x,y):
      return  x+y

print(add2(5,7))

'''
定义可以修改装饰器的参数
'''