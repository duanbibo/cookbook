from itertools import  product ,permutations,combinations

'''
排列组合: 多个可迭代对象的排列组合 ，排列的情况大于组合的情况。 
                可以对可迭代对象进行取部分数据参与排序或者组合
permutations :将可迭代对象中的各个对象进行排列，考虑顺序
combinations: 组合，各个元素的组合，不考虑顺序如 a,b 和 b,a属于一种   ,组合时必须要指定可迭代对象参与的序列长度
product :将多个可迭代对象每个取出一个数据，参加迭代组成一个新的情况。一般用于矩阵
'''

ite1=[1,2,3,4]
paixu=0

#在for循环里面遍历
for i in permutations(ite1):
      print(i)
      paixu+=1
print(paixu)


zuhe=0
for i in combinations(ite1,3):
      print(i,end='..')
      zuhe+=1
print(zuhe)

iter2=['a','b','c']


for i in product(ite1,iter2,repeat=2):
      print(i)