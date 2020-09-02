from functools import wraps

'''

类装饰器：
分为两种： 第一种就是类中的某个方法为装饰器方法，这个方法可以是普通方法，也可以是静态方法。
            使用方面也有区别，如果是普通方法：通过初始化类实例，使用@实例.装饰器方法
                           如果是静态方法：可以直接通过@类名.静态方法区使用，
         第二种就是整个类作为一个装饰器，在使用上直接通过@类名
'''


class A:
      #定义的类普通装饰器
      def decorator1(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                  print('Decorator 1')
                  return func(*args, **kwargs)

            return wrapper

      #定义的静态装饰器
      @classmethod
      def  decrotor2(cls,func):

            @wraps(func)
            def wrapper(*args,**kwargs):
                  print('Decorator 2')
                  return  func (*args,**kwargs)
            return wrapper



#通过实例调用
a=A()
@a.decorator1
def spam1():
      print('decortor1')

#通过类调用
@A.decrotor2
def spam2():
      print('decortor2')


spam1()
spam2()

'''
将装饰器定义为类
   使用一个装饰器去保证函数，希望返回一个可调用的实例。需要让你的装饰器可以同时工作在类定义的内部和外部。 
   
   为了将装饰器定义成一个实例，你需要确保它实现了  __call__ 和  __get__ 方法。
     使用get 描述符的作用是为了解决，在实例内 通过func.(arg,kwargs)时，返回的实例是装饰器本身实例，而非被修饰的实例。
     需要先通过 __get__描述符获取到instance，然后再传给 __call__ 函数的self。进行绑定

'''
import  types

class Prifiled:

      def __init__(self,func):
            wraps(func)(self)
            self.ncalls=0

      def __call__(self, *args, **kwargs):
            self.ncalls+=1
            return self.__wrapped__(*args,**kwargs)
      def __get__(self, instance, owner):
            if instance is None:
                  return  self
            else:
                  return  types.MethodType(self,instance)

'''
将装饰器使用到类上的普通方法和静态方法，类方法，必须写在他们的前面，即内部
'''