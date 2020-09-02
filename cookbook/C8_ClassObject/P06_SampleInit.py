

'''
定义个公共的类，简化init，保持参数顺序和数量，使用zip组合

'''
class  Structure:

      _fields=[] #定义的参数，初始化时直接传就可以了，对应的是init内的args

      def __init__(self,*args,**kwargs):
            if len(args)!= len(self._fields):
                  raise TypeError('参数数量不正确')

            #保持参数顺序和数量，使用zip组合,
            for name,value in zip(self._fields,args):
                  #通过调用setattr内建函数，为对象动态添加属性和值
                  setattr(self,name,value)

            #对于传入的额外关键字参数进行处理
            #这一步处理时因为，对于传入的关键字参数也有可能是本来支持的参数。
            #如 fields内定义了name属性，但是调用的时候通过name='zs'传了，这一步需要把他给过滤掉
            extra_args = kwargs.keys() - self._fields

            for name in extra_args:
                  #这里通过列表的pop依次取出元素，为属性设置值
                  setattr(self,name,kwargs.pop(name))

            #检查是否还有其他未处理参数
            if kwargs:
                  raise TypeError('错误')


class Person(Structure):
      _fields = ['name','age','info']

p=Person('zs',18,"good student",tel="110")
print(p.age)
print(p.tel)

