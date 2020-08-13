

'''
编写代理迭代： 将iter函数和 next函数写在不同的类里面，第一个类编写iter魔法函数，iter中返回第二类的实例
         第二个类编写next()函数，编写自己的next魔法函数，
                  魔法函数中定义循环进行迭代，循环外必须引发迭代停止异常，然后就会停止。
       使用：创建第一个类的对象，遍历类对象。

'''

'''
通过 iter函数创建可迭代对象 iter 函数有两个参数，第一个是个object，第二个是哨兵，作为结束事件。
'''




class Ite:
      def __iter__(self):...
      def __next__(self): ...

''' 迭代实例'''
class diedai:
      '''
      自定义的迭代对象：必须要同时重载iter和next方法，才是一个迭代对象。
      迭代对象 iter负责产生数据迭代对象，next负责拿到这个数据。
      iter的返回部分可以是其他对象的实例，然后next可以在这个对象内。实现
      在这里时，iter负责返回对象本份，next对数据进行加工处理。
      当创建实例后，调用next时，直接执行next
      当遍历的时候，调用for range时，是先执行iter部分

      '''

      def __init__(self,start,stop):
            self.value=start-1
            self.stop=stop
      def __iter__(self):
            ''''''
            return self

      def __next__(self):
            '''进行迭代的时候必须引发异常，进行停止迭代。'''
            if self.value==self.stop:
                  raise StopIteration
            else:
                  self.value+=1
            return  self.value

class  prx():
      def __init__(self):
            self.value=Node()

      def __iter__(self):
            return  self.value

class Node:
      def __init__(self):
            self.value=5

      def __next__(self):
            while self.value>0:
                  self.value=self.value-1
                  return self.value
            raise  StopIteration()


if __name__ == '__main__':
      from collections import Iterator, Iterable
      #当前类只要有iter魔法方法就是可迭代对象
      p=prx()
      print(isinstance(p,Iterable))
      print(isinstance(p, Iterator))
      for i in p:
            print(i)

      #当前类必有iter方法和next方法都拥有，他才是一个迭代器
      I=Ite()
      print(isinstance(I, Iterator))
