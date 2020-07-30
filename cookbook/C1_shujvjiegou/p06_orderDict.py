from  collections import OrderedDict
from  itertools import groupby


'''
有序字典创建的是按照插入的时间进行排序的，空间是平常字典的2倍，因为内部需要额外维护一张链表

'''

a=OrderedDict()
a['2']=2
a['1']=1
print(a,type(a),type(a.keys()))


''' 使用chainmap 拼接合并字典 :即使key相同也不会覆盖 ,打印输出key时，返回最先出现的那一个。
   chainmap只是简单维护一个记录底层映射关系的列表，然后重新定义常见的底子安
'''
from  collections import ChainMap
dicta={'a':'1'}
dictb={'b':2}
dictc={'b':3}
dictd={'d':4}
hebing=ChainMap(dicta,dictb,dictc,dictd)
print(hebing,hebing['b'])

print(hebing.maps,"获取结果转化为list",type(hebing.maps))
print(hebing.parents)

''' 另一种方式回顾：使用字典的update方法
  update方法：可以将另一个字段的key：value 传入自己内，如果键相同值覆盖。破坏了原始数据
'''
dictc.update(dictb)
print(dictc)



