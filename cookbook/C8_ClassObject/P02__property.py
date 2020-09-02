import math

'''
perperty的作用：把类伪装成属性调用，提供get,set,del方法

'''


class Circle:

      def __init__(self, radius):
            self.radius = radius

      # 这种方式更好
      @property
      def area(self):
            return math.pi * self.radius ** 2

      def mianji(self):
            return math.pi * self.radius ** 2


c = Circle(5)
print(c.area)
print(c.mianji())




class Person:
      def __init__(self, name):
            self.name = name

      # Getter function
      @property
      def name(self):
            return self._name

      # Setter function，设置赋值规则
      @name.setter
      def name(self, value):
            print('base.set')
            if not isinstance(value, str):
                  raise TypeError('Expected a string')
            self._name = value

      # Deleter function ,限制删除
      @name.deleter
      def name(self):
            raise AttributeError("Can't delete attribute")

p=Person('str11')
p.name='tom2'
print(p.name)



'''
在子类中，可以扩展父类中的property功能:
  在内部调用super的基础后面调用魔法函数__set__


'''
class SubPerson(Person):
      ...

      @property
      def name(self):
            print('Getting name')
            return super().name


      #重新父类的property方法，对名字的长度做限制
      @name.setter
      def name(self, value):
            print('Setting name to', value)
            if len(value)<=3:
                  raise ValueError("名字太短了")
            else:
                  self.name=value

      @name.deleter
      def name(self):
            print('Deleting name')
            super(SubPerson, SubPerson).name.__delete__(self)


#子类默认是不继承父类的property限制的
s=SubPerson('14')
print(s.name)

s.name='zs'
print(s.name)



p
'''
在子类中扩展一个 property 可能会引起很多不易察觉的问题，因为一个 property
其实是 getter、setter 和 deleter 方法的集合，而不是单个方法。因此，当你扩展一
个 property 的时候，你需要先确定你是否要重新定义所有的方法还是说只修改其中某
一个。

  如果在子类中只覆写一个的话，需要这样写
  @Person.name.getter
  def name(self)：
                     不能只写覆盖的，否则get方法也消失了，这样写父类之前定义的方法也会被赋值过来，而getter函数被替换

'''
class SubPerson2(Person):
      ...

      @Person.name.getter
      def name(self):
            print('Getting name')
            return super().name


s2=SubPerson2('li')
print(s2.name)
s2.name="dd"
print(s2.name)

