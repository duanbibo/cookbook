import sys

'''

默认参数的陷阱，对应可变类型的参数，一定不要写  b=[]  ,而要写b=None
    当你在函数内使用了b=[]为变量设置一个空类型的列表，当多次调用这个函数时，下次调用时这个函数的默认值就会发生变化。


def在Python中是一个可执行的语句，当解释器执行def的时候，
默认参数也会被计算，并存在函数的.func_defaults属性中。
'''

def appendtest(newitem,lisa=[]):
      invar=5
      print(id(lisa))
      lisa.append(newitem)
      print(id(lisa))
      return lisa

a=appendtest('a',['b',1,2,[3,4]])
print(a)
a.append('d')
print(a)
print(appendtest.__code__.co_varnames,"函数的所有变量：包括参数列表和内部变量")
print(appendtest.__code__.co_freevars,"函数内部的自由变量")
print(appendtest.__code__.co_names,"函数内部使用的func")
print(appendtest.__code__.co_name,"函数的名称")
print(appendtest.__code__.co_consts,"函数的内部常量")
print(appendtest.__code__.co_firstlineno,"函数的第一行在文件中的行号")
print(appendtest.__code__.co_argcount,"函数的参数列表数量")
print(appendtest.__qualname__,"函数的全限定名")
print(appendtest.__code__.co_filename,"函数所在文件夹的位置")

#
# def dfunc(a,b=[]):
#       print(b)
#       return b
#
# x=dfunc(1)
# print(dfunc.func_defaults)
# x.append(99)
# x.append('yow')  #下次在调用时默认参数会发生变化。
# print(x)
