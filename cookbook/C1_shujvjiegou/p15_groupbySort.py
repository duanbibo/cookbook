from itertools import  groupby
from operator import itemgetter ,attrgetter

'''对数据进行分组'''

rows = [
      {'address': '5412 N CLARK', 'date': '07/01/2012'},
      {'address': '5148 N CLARK', 'date': '07/04/2012'},
      {'address': '5800 E 58TH', 'date': '07/02/2012'},
      {'address': '2122 N CLARK', 'date': '07/03/2012'},
      {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
      {'address': '1060 W ADDISON', 'date': '07/02/2012'},
      {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
      {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


g=groupby(rows,key=lambda x:x['date'])
#输出的结果第一个是分组标准，第二个是分组后的其他字段对象。

for i in g:
      print(i[0],list(i[1]))

'''
排序： 对可序列的类型可以用operator库中的 itemgetter()函数，指定可迭代对象中的下标或者键名
         itemgetter()本身是根据可迭代对象，进行构建一个新的指定的迭代对象，
         用在groupby,sorted 中当key的值，可以根据可迭代对象的当前字段值进行排序或分组。
       对于不可序列的类型排序，如对象Person,可以利用attrgetter()函数指定对象的实例属性。

'''
#如果单独使用分组的话，前后两个不连续的，但是字段一样的，会导致不在一个组中。
#所以需要在分组前先进行排序。利用 sorted排序 itemget指定字段或者lambda表达式函数指定字段

paixu=sorted(rows,key=itemgetter('date','address'))
print(paixu)
print("=====================2个字段，起冲突后根据第二个字段升序排")

iterlist=[
      [1,2,3,4,5],
      [6,7,8,9,10],
      [4,3,4,5,6],
      [4,2,4,5,7]

]

paixu2=sorted(iterlist,key=itemgetter(4,3))  #如果可迭代对象的内部是列表的话，里面传列表的索引

print(paixu2)





#使用lamdaba表达式，x指的是前面的可迭代对象，根据可迭代对象的‘date’键进行排序
p=groupby(paixu,key=lambda x:x['date'])
for i in p:
      print(i[0],list(i[1]))


''''
利用 operator 中的 attergetter 对object 指定的属性排序  ，构造函数实例绑定的属性, 需要借助可迭代对象，
                   sorted(iterable, key=attergetter( 'attr'))
'''
class  person:

      def __init__(self,id,name):
            self.id=id
            self.name=name
      def  __str__(self):

             return  " id: %s,姓名: %s" %(self.id,self.name)

      def __repr__(self):
            return repr(( self.id,self.name))

p1=person('001','zhangs')
p2=person('002','lisi')
p3=person('003','wangwu')
p4=person('004','zhaoliu')
P=[p1,p2,p3,p4]

pname=sorted(P,key=attrgetter('name'))
print(pname)

