import  heapq


'''
堆 :查询集合中最大/小的部分数据，它内部有方法，传入集合源数据和需要查找的几个最值

查找集合中最大或者最小的N个元素
另一种方式，对集合进行排序然后使用切片
当只查找一个时，可以用内置的max  min方法



'''
nums=[-4,23,109,32,4,-6,5,23]

''' 查找集合中最大的4个元素'''

print(heapq.nlargest(4,nums))    # 你个 最大的数字   n  gt  est
print(heapq.nsmallest(2,nums))   #最小的            n   smal  lt
'''
关键参数key，还能够在更为复杂的数据结构上输出,与sorted的关键字key类似
           参数都是 实例的可迭代对象，以及可以与可迭代对象交互的lambda函数

'''
portfolio = [
      {'name': 'IBM', 'shares': 100, 'price': 91.1},
      {'name': 'AAPL', 'shares': 50, 'price': 543.22},
      {'name': 'FB', 'shares': 200, 'price': 21.09},
      {'name': 'HPQ', 'shares': 35, 'price': 31.75},
      {'name': 'YHOO', 'shares': 45, 'price': 16.35},
      {'name': 'ACME', 'shares': 75, 'price': 115.65}
]



hg=heapq.nlargest(3,portfolio,key=lambda s:s['shares'])
print(hg)



'''
通过某个键的值，进行排序：
 第一种：利用sorted 的key 指定可迭代对象的key值，获取key的键，根据键排序
'''
s=sorted(portfolio,key=lambda s:s['price'])  #默认升序
print(s)

#第二种：使用itemgetter 构建新的列表。  operator库主要提供了简便的操作，
#提供一些简便的操作类和函数，能代替从序列中取出元素或者读取出对象属性的lambda表达式。

from operator import itemgetter

si=sorted(portfolio,key=itemgetter('price'))  #他也是利用了可迭代对象,


li=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
er=itemgetter(0,2) #这里构建了个函数，返回一个生成器函数
print(er)
it=er(li)
print(it)     #([1, 2, 3, 4], [9, 10, 11, 12])




