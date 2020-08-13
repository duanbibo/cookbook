import heapq
from itertools import zip_longest


'''
利用堆的函数 merge，将多个可迭代对象添加入堆中
   要求可迭代对象本身是有序的   
'''
l1=[1,4,5,7,9]
l2=[2,3,6,8]

print( "使用堆的merge方法时，必须保证多个序列内的数字为有序的")
for i in heapq.merge(l2,l1):
      print(i)

''' zip_longest :将多个可迭代对象组合，与zip相比可以添加如果长短不一致时的，默认值'''
zl=zip_longest(l1,l2,fillvalue='novalue')
print(list(zl))