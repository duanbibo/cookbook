

'''
编写代理类，通过在代理方法—__init__内引用被代理类的实例，

   适用场景：一个类中需要被代理的方法较少，在代理类中只声明同一个方法名。然后return过去就可以了



'''

class A:
      def spam(self,x):
            print("原始类的方法")

            pass
      def foo(self):
            print("原始类")


class B:
      #通过当前类构造器中的定义的属性，引用其他类，在当前类方法中调用其他类的
      def __init__(self):
            self._ab=A()

      #代理类，写的方法名一样，但是里面没有任何逻辑，直接通过实例调用被代理类的昂发、
      def spam(self,x):
            print("代理类")
            return  self._ab.spam(x)

b=B()
b.spam('5')


'''
弊端：考虑到代码量，如果被代理类中需要被代理多个方法，这样写需要大量的代理需要，可以通过 __getattr__ 代理在init方法内
     传入的实例对象的所有方法
     __getattr__ : 访问拦截不存在的属性
'''

class B2:
      def __init__(self):
            self.a=A()

      def bar(self):
            print("self")

      #通过魔法函数，就不可以不需要显式指定了
      def __getattr__(self, item):
            return getattr(self.a,item)
b2=B2()
b2.foo()


'''
代理模式：
            通过定义一个基类包装类，内部实现 魔法方法 __setattr__ ,__getattr__ ,__delattr__
            
            其他类创建对象后，将对象传入这个基本中，能够实现对对象所有属性的控制，是否进行添加、更改、删除属性，最后通过调用
            getattr(object ,attr[,default])  setattr(object,attr,name)
            
            目的：通过外部代理类也能够访问原类中所有的属性和方法
            
'''

class  Proxy:


      def __init__(self,instance):
            #这个参数代表包装类的实例
            self._instance=instance


      #这个拦截实例不存在的属性
      def __getattr__(self, item):
            print('getattr',item)
            return getattr(self._instance,item)

      #注意的是，通过setattr调用时，会调用getattr的，会造成死循环
      def __setattr__(self, key, value):
            #print('setattr:{},{}'.format(key,value))
            #return setattr(self._instance,key,value)
            if key.startswith('_'):
                  super().__setattr__(key,value)
            else:
                  print('settr:',key,value)
                  setattr(self._instance,key,value)
class Spam:
      def __init__(self,x):
            self.x=x

      def bar(self,y):
            print('Spam.bar:',self.x,y)


s=Spam(5)
p=Proxy(s)
p.x
p.bar(4)

#可以动态的获取额外值
p.name='lisi'
p.name


