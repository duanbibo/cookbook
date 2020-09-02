

'''
property
'''
'''
property 的特性，子类继承，子类重写
'''
class  base:

      def __init__(self):
            print("base")

      def info(self):
            print("base method")

class son(base):

      def __init__(self):
            print('son')
            super().__init__()  #使用super函数传，如果有多继承的话，自动寻找继承体系。MRO方法解析顺序
            print(son.__mro__)
            base.__init__(self)  #使用父类传，必须传入未绑定方法，传入子类实例
            print(son.__mro__) #查看

      def info(self):
            super().info()  #调用父类的方法
            print("son info")

s=son()
s.info()

print("==============多继承")
'''
多继承的MRO方法解析顺序： 菱形继承
  通过类名.__mro__ 可以查看当前类继承的列表，默认是根据这个列表进行搜索的。
 
  在多重继承中，使用super()函数，避免了对共同父类的父类构造器多次调用。
   对于base类而言，只会被初始化1次。
                base()
                print('base.__init__')
                
    A(base)                               B(base)
      super().__init_                         super().__init_
      
                   C(A,B) 
                     super().__init_
 
'''

class  ba:
      def __init__(self):
            print('base.__init__')
class A(ba):
      def __init__(self):
            super().__init__()
            print('A.__init__')
class B(ba):
      def __init__(self):
            super().__init__()
            print('B.__init__')
class C(A,B):
      def __init__(self):
            super().__init__()
            print(C.__mro__)
            print('C.__init__')

c=C()



