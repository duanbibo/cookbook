
'''

使用生成器 对数字进行转换和计算
'''
lt=[1,2,3,4,5,6]
'''求平方和'''
he=sum( i*i for i in lt)

'''  第二种方式：先用map函数对可迭代对象进行平方，再用reduce进行累加'''
from functools import  reduce
m=list(map(lambda x:x*x,lt))
print(m)
#reduce函数，将迭代对象前后两个数进行某种运算，一般用于累加
r=reduce(lambda x,y:x+y,m)

print(he,r)
