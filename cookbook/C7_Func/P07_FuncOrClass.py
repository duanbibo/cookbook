import threading
'''

将类方法转化为函数:
    大部分情况下，拥有类方法的原因是需要存储某些额外的状态来给方法使用。以便将来在方法中使用。
    如果一个类中只有一个类方法，我们可以通过闭包的方式来满足这种情况。
    如果选择了函数后，类的特性如继承、属性、描述符、类方法都是不能用的。

'''

class People():

      def __init__(self,name,age):
            self.name=name
            self.age=age

      def info(self):

           return print(self.name,self.age)

p=People('zs',27)
p.info()


'''
分析下：threading模块，通过函数或者类创建线程 ，我们更喜欢通过函数的方式来创建。
  既然线程只需要运行一个func，可以直接通过函数的方式运作,
  threading模块的Thread类核心就是run方法，执行。
  他在源码中是通过run方法，执行 构造函数中的 target(args ,**kwargs),在内部调用的

'''
num=0
def func(x):
   global  num
   while num<x:
         num += 1
         print(num)

t=threading.Thread(target=func,args=(5,))
t.start()



'''
闭包： 函数包括函数，闭包能够获取外部的func，参数列表，并且支持调用他们
'''
def people(name,age):
      def info():
           print(info.__closure__,"打印闭包支持访问的变量，只要返回不为None,就是闭包")
           print(len(info.__closure__),"cell中有3个，包括外层的func,和外层的参数,")#func:people(name,age)
           print(name,age)

           #return (name,age)
      return info

pf=people('zs',28)
pf()






