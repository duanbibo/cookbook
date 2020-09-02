
'''
创建类的实例属性  ,通过其他类的 set ,get ,del

  属性源自其他类的实例。
  1.声明通过其他类编写get,set,del等魔法函数
  2.引用：本类中，创建全局属性，=右侧取自其他类的实例
  3.调用生效：本类中，通过创建实例，调用类的全局属性，调用

  描述符： 关系：描述类 。包含set ,get ,del的类
               调用类 ：  将描述类的实例当做类属性

  简书：描述符设计到元编程，装饰器，


'''

class Integer:


      def __init__(self,name):
            self.name=name

      #使用描述符：形参instance代表 ，调用此类的实例
      # cls代表：
      def __get__(self, instance, cls):
            print("调用属性的get方法")
            if instance is None:
                  return self
            else:
                  #核心是这块，通过调用类实例的__dict__魔法函数，为其添加key,value
                  return instance.__dict__[self.name]

      def __set__(self, instance, value):
            if not instance(value,int):
                  raise TypeError('Execpt an int')

            # 核心是这块，通过调用类实例的__dict__魔法函数，为其添加key,value
            instance.__dict__[self.name]=value


            # hasattr(instance,self.name)
            # getattr(instance,self.name,'default')
            # setattr(instance,self.name,'value')
class Point:
      x=Integer('x')
      y=Integer('y')

      def __init__(self,x,y):
            self.x=x
            self.y=y


class lazyperperty:
      def __init__(self,func):
            self.func=func

      def __get__(self, instance, owner):
            if instance is None:
                  return self
            else:
                  value = self.func(instance)
                  setattr(self,self.func.__name__,value)
                  return value

import math
class Cricle:
      def __init__(self,radius):
            self.radius=radius

      @lazyperperty
      def area(self):
            print("Computing area")
            return  math.pi*self.radius**2


c=Cricle(3)
print(c.area)
print(c.__dict__)
print(vars(c))

#弊端，创建的方法当做属性时，可以通过赋值直接修改，可以对代码优化下，通过hasattr  进行判断，有的话就
c.area=90
print(c.area)

#dir打印对象的属性列表，包括魔法函数
print(dir(c),c.__dir__())

