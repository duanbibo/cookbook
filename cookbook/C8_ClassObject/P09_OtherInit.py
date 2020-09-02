from time import  localtime

'''

通过其他方式进行初始化

1. 正常通过init方法对实例进行初始化
2.可以直接调用 _new__方法创建实例， 然后利用setattr,为这个实例赋init内相同的值
3.通过静态方法，在静态方法内部为返回的类实例赋同样的值，类方法调用时 不能加括号，否则走的是创建实例的过程。


'''



class Date:

      def __init__(self,year,month,day):
            self.year=year
            self.month=month
            self.day=day

      @staticmethod
      def staMeth():
            print("静态方法不需要实例化，同时没有绑定类名和类实例，调用时通过类名.statMeth()")


      #类方法，可以直接通过类名调用,类后面不需要 括号 .调用时， 类名.classMeth() ,
      #类方法，主要目的是仿照java的多构造器，在内部可以调用__new__方法，返回类对象，在对类对象赋值。产生实例。
      @classmethod
      def today(cls):
            d=cls.__new__(cls)
            t=localtime()
            d.year=t.tm_year
            d.month=t.tm_mon
            d.day=t.tm_mday
            return  d

      def when(self):
            return (self.year,'-',self.month,'-',self.day)


#init方法创建实例
i=Date(2018,4,8)
print(i.when())



#__new__放啊也是个静态方法，第一个参数绑定了类名，所以在调用__new__方法是必须传入一个类名
#通过调用new方法，传递类名，然后为返回的类对象进行赋值，实际也是隐式的调用了init方法
d=Date.__new__(Date)
print(d)

data={'year':2010,'month':8,'day':27}
for key,value in data.items():
      setattr(d,key,value)

print(d.month)
print(d.when())

#类方法调用
td=Date.today()
print(td.year,td.month,td.day)