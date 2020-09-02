import time


'''

混合类:

 出现的背景：    一个类中有很多有用的方法，想使它们来扩展其他类的功能。但是这些类并没有任何继承关系。
                因为你不能简单的将这些方法放入一个基类，然后被其他类继承。
 解决方案：
               通常当你想定义类的时候还会碰上这些问题，可能是某个库提供了一些基础类，你可以利用它们来构造你自己的类。
               假如你想扩展映射对象，给它们添加日志、唯一性设置、类型检查等等功能。
               
 混入类的声明要求：  混入类Mixin是不能直接被实例化的，内部不能定义 __init__()方法，并且没有实例属性。
 
 使用混入类要求： 
             使用混入类的类，必须有混入类和非混入类。第一个必须为混入类，有init方法的其他类放在最后
             根据多继承原则，初始化使用的为非混合类，在调用初始化方法，由于混入类没有init方法，所以去找其他非混入类的init方法。
             在使用方法方面，通过初始化的对象，能够调用混入类的方法，更可以调用初始化类对象的方法。
             


'''


class  LoggedMappingMixin:

       __slots__ = ()   #混入类都没有实例变量，因为直接实例化混入类没有任何意义

       def __getitem__(self, item):
              print('getting'+str(item),"通过混入类的__getitem__方法获取键值对")

              return super().__getitem__(item)

       def __setitem__(self, key, value):
              print('Setting {} = {!r}，"通过混入类的__setitem__方法为字典添加属性值"'.format(key, value))

              return super().__setitem__(key, value)

       def __delitem__(self, key):
              print('Deleting ' + str(key))

              return super().__delitem__(key)


class  SetOnceMappingMinxin:

       __slots__ = ()

       def __setitem__(self, key, value):
              if key in self:
                     raise KeyError(str(key) + ' already set')

              return super().__setitem__(key, value)

class StringKeysMappingMixin:
       __slots__ = ()

       def __setitem__(self, key, value):
              if not isinstance(key, str):
                     raise TypeError('keys must be strings')

              return super().__setitem__(key, value)

#这些类单独使用起来没有任何意义，事实上如果你去实例化任何一个类，除了产生异常外没有任何作用，
#他们是用来通过多继承来和其他映射对象混入使用。

#如何混入？  混合类没有init方法，主要提供一些操作工具类。
class LoggedDict(LoggedMappingMixin,dict):
      pass



d=LoggedDict()
d['x']='1'
print(d['x'])
print(d,d.__class__)


#设置默认字典，控制value的类型,类型为list
from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMinxin, defaultdict):
                     pass

sd=SetOnceDefaultDict(list)
sd['k'].append(2)
sd['k'].append(3)
print(sd,sd.__class__)


