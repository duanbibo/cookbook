import linecache

'''
闭包的实例
'''

g=1
def  out():
      o=2
      def inner():
           d=g+o
           print(d)


      return inner

ot=out()
ot()



'''
访问闭包中的变量

   编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的

'''
def sample():
      n=0

      #闭包的函数
      def func():
            print('n=',n)

      #为闭包提高的函数属性
      def get_n():
            return n
      def set_n(value):
            nonlocal n
            n=value

      #绑定属性
      #为闭包函数绑定一个属性，这个属性是其他的函数，和实例方法很像self.info ...

      func.get_n=get_n
      func.set_n=set_n

      return func

s=sample()
s()
s.set_n(5)
s()

'''

闭包的高级运用:给闭包添加方法会有更多的实用功能，比如你需要重置内
部状态、刷新缓冲区、清除缓存或其他的反馈机制的时候
'''

