from itertools import dropwhile ,filterfalse,takewhile

'''
dropwhile:跳过可迭代对象中的前一部分元素，

dropwhile(func,iterable):
 对可迭代对象进行过滤，                     如果符合func返回结果为true时，进行跳过不输出值。
  只过滤一次，当出现失败的时候后面的数据都不过滤了。 
  实用性非常强，避免了代码中的if  starwith 。。break  语句

'''


def count(n):
      while n>0:
            yield  n
            n-=1
n=count(20)

''''''
d=dropwhile(lambda x:x>6,n)
print(list(d))

'''
takewhile : 一次过滤失败，出现失败时停止，返回成功符合的数据。与 dropwhile 相反
'''

li1=[25,77,0,-2,3,0,6,4,-4,8,7,2]
print(list(takewhile(lambda x:x>2,li1)),"takewhile 从开头只取成功的数据")

dw=dropwhile(lambda x:x>2,li1)
print(list(dw)," drop while一次判断获取不符合的数据后面的所有部分")

'''
filter  与 filterfalse 两个相反
'''
f=filter(lambda x:x>2,li1)
print(list(f))

f=filterfalse(lambda x:x>2,li1)
print(list(f))