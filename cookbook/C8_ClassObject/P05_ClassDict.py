

class Person:

      school='Middle'

      def __init__(self,name,age):
            self.name=name
            self.age=age

      def info(self,tel=None):
            print(tel)

p=Person('zs',23)

def func():
      ...

a=45
'''
本质上 vars 和 __dict__ 是一样的，如果传参和同通过对象调用，打印的结果相同
        如果不传参，vars打印的是当前模块内所有的字典信息；而__dict__必须接受传参
        如果对象没有__dict__方法， 通过vars调用会报错TypeError: vars() argument must have __dict__ attribute
        
'''
print(vars(Person))
print(Person.__dict__)
print(vars(func),func.__dict__)
print(vars(a))