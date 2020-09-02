from itertools import islice
from itertools import count
from operator import itemgetter


'''
对迭代对象做切片操作： islice
 由于生成器和迭代器产生的数据是产生就释放的，普通的方式是不可能捕获到的，

'''

def Count(n):
      while n>0:
            yield  n
            n-=1
n=Count(20)
print(n)
# for i in n:
#       print(i,end='..')
lice=islice(n,0,10) #捕获到迭代进行的第5次到第10次之间的数据，第
print(list(lice))

''' 使用itemgeter 结合 sorted，对可迭代对象进行排序'''


''' 使用 count试下:无限生成器,生成出来的对象必须通过for循环遍历。'''


c=count(5,7)

for i in c:
      if i<100:
            print(i)

#内部实现结果
def count1(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step


