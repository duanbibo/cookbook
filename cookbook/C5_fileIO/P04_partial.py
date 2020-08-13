from functools import partial


'''
冻结参数 ，返回一个新的函数对象，这个函数对象能够调用内部的func，且将parameter进行绑定，
   在调用这个冻结函数时，只需要传一个参数就可以了

 语法    partial(oldfunc  , parameter)
'''

nt=partial(int,base=8)
print(nt('23'))

from operator import mul
#mul:两数的成绩
su=partial(mul,20)
print(su(5))