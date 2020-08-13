from itertools import islice

'''
对迭代对象做切片操作：
 由于生成器和迭代器产生的数据是产生就释放的，普通的方式是不可能捕获到的，

'''

def count(n):
      while n>0:
            yield  n
            n-=1
n=count(20)
print(n)
# for i in n:
#       print(i,end='..')
lice=islice(n,0,10) #捕获到迭代进行的第5次到第10次之间的数据，第
print(list(lice))