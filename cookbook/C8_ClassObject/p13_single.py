import weakref

'''
弱引用: 当一个对象的引用只有弱引用时，垃圾回收机制把这个对象不用的时候销毁，把内存用于其他地方。
 弱引用其中一个用途是用于实现大对象的缓存或者映射，由于是缓存火映射，对象不需要独立存在。
 并不是所有对象都支持弱引用，例如列表和字典不能够直接支持弱引用，但是可以通过子类支持。
   其他的内置类型诸如元组和long，即使通过子类的方式也不能够进行弱引用。
   
 class weakref.ref(object[, callback]) ,创建一个弱引用。
             object是被引用的对象，callback是回调函数，当引用对象被删除时，会调用回调函数
             
   class weakref.WeakKeyDictionary([dict])， 创建key为弱引用对象的字典
   class weakref.WeakValueDictionary([dict])， 创建value为弱引用对象的字典
             
 Python weakref中提供WeakKeyDictionary和WeakValueDictionary两个类用于构建非长久驻留内存的对象。
 当最后一次引用之后，垃圾回收机制会回收其内存。而相应的映射关系也会被删除。
 这两个类在实现的时候使用了弱引用，并设计了垃圾回收弱引用字典时的回调通知函数。


'''

'''

创建缓存实例，在创建一个类的对象时，如果之前使用同样参数创建过这个类，你想返回它的缓存引用

'''
import logging

from cookbook.C8_ClassObject.P12_MethodCaller import Point

a=logging.getLogger('foo')
b=logging.getLogger('foo')
print(a is b)

p1=Point(2,3)
p2=Point(2,3)
print(p1 is p2)

'''
使用弱引用
'''
class SpamWerk:

      #类中使用一个常量字典存储多个new返回实例的结果
      _spam_cache = weakref.WeakValueDictionary()

      def __new__(cls, name):

                  if name in cls._spam_cache:
                        return cls._spam_cache[name]
                  else:
                        self = super().__new__(cls)
                        cls._spam_cache[name] = self
                        return self

      def __int__(self,name):
            self.name=name

S1=SpamWerk('Dave')
S2=SpamWerk('Dave')
S3=SpamWerk('Dave3')
print(S1 is S2)
print("使用弱引用-下面打印弱引用的key值")
print(list(SpamWerk._spam_cache.keys()))
del S2
print(list(SpamWerk._spam_cache))








'''
很多库中都有实际的例子，使用相同的名称创建的实例永远只有一个。
  可以利用类变量，存储一个字典，利用 __new__ 魔法函数，当不存在时，将参数组成的key添加到字典内，值就是self，返回self
                                          判断字典内是否有多个参数组成的key,如果存在，就直接返回参数组成的key对应的值，也就是self
'''


class Spam:

      #类中使用一个常量字典存储多个new返回实例的结果
      _spam_cache = {}

      def __new__(cls, *args, **kwargs):

                  if args in cls._spam_cache:
                        return cls._spam_cache[args]
                  else:
                        self = super().__new__(cls)
                        cls._spam_cache[args] = self
                        return self

      def __int__(self,name):
            self.name=name


s1=Spam('001')
s2=Spam('001')
s3=Spam('003')
s4=Spam('004')
print(s1 is s2)
print(Spam._spam_cache)

del s1


'''
使用全局变量，并且工厂函数跟类放在一起，可以通过将缓存代码放到一个单独的缓存管理器中：


'''

#缓存管理器。存放多个类的实例
class CachedSpamManager:

      def __init__(self):

            self._cache = weakref.WeakValueDictionary()


      #这里被硬编码了，主要理解模式，将这个类当做其他类的常量
      def get_spam(self, name):

            if name not in self._cache:
                  s = Spam(name)
                  self._cache[name] = s
            else:
                  s = self._cache[name]
            return s

      def clear(self):

            self._cache.clear()


class Test1:

      #工厂函数
      manager = CachedSpamManager()

      def __init__(self, name):
            self.name = name

      def get_spam(name):
            return Test1.manager.get_spam(name)


class Test2:
      # 工厂函数
      manager = CachedSpamManager()

      def __init__(self, name):
            self.name = name

      def get_spam(name):
            return Test2.manager.get_spam(name)



