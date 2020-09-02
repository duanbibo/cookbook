

class Pair:

      #使用插槽，限定只能访问这些属性名。主要目的是使实例更加紧凑，大量节省内存空间。
      #使用后就无法通过__dict__进行访问了
      __slots__ = ['x','y']

      def __init__(self,x,y):
            self.x=x
            self.y=y
      def __str__(self):
            #通过字典的索引，打印第一个字典的x对应的值。 0代表format内的列表中那一组字典。
            #  ！s ，使用format格式字符串，转换 ！r调用 reper()  !s调用str() ,!a 调用ASCII()
            return '({0.x!s},{0.y!s})'.format(self)
      def __repr__(self):
            return'Pari {},{}'.format(self.x,self.y)



p=Pair(3,4)
print(p,type(p.x))