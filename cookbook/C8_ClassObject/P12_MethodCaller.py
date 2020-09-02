from operator import methodcaller ,attrgetter

'''
类方法引用 和函数 属性引用
methodcaller  ,  attrgetter
用法：   md=methodcar('funcName','Parm1','Parm2'...)         md(instance)  调用当前的方法
      
        eg:  类似于java的方法引用，它创建的是一个可调用对象。在声明时只说明固定的func的名字和func对应的参数列表.
          在传入实例时直接调用声明的func的名字和参数列表。
               

   
        atr=attrgetter('self.attr')       属性引用一般用在排序上如：   sorted(SomeInstance,key=atr)
            对这些类的此属性进行排序
            或者使用栏目表达：   sorted(SomeInstace,key=lambda x:x.Age)   .对实例的Age属性进行排序
'''
import math

class Point:
      def __init__(self,x,y):
            self.x=x
            self.y=y

      def __repr__(self):
            return  'Point (!r:),(!r:)'.format(self.x,self.y)

      def distance(self,x,y):
            return math.hypot(self.x-x,self.y-y)



p=Point(2,3)
#利用getattr方法，获取类实例的方法，并且给他传参
d=getattr(p,'distance')(0,0)
print(d)

#methodcaller('引用的方法名'，’当前方法的引用形参‘...) 返回这么一个对象，这个对象直接传入
m=methodcaller('distance',0,0)
m1=m(p)
print(m1)