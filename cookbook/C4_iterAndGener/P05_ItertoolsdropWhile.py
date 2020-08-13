from itertools import dropwhile

'''
dropwhile:跳过可迭代对象中的前一部分元素

dropwhile(func,iterable):
 对可迭代对象进行过滤，如果符合func返回结果为true时，进行跳过不输出值。
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