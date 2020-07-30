
'''
具名元祖  :使用具名元祖为各个字段命名，解决数据库和面向对象的问题
'''
'''
讨论：具名元祖是作为字典的代替，后来需要更多地空间来存储，
    因此如果需要构建涉及字典的大型数据结构，使用具名元祖会更加高效。
    同时具名元祖满足了元祖的不可变性，做到了安全。
'''
from collections import  namedtuple

info=namedtuple("info","name age tel")
one=info("张三",20,110)
print(one)
#one.age=90   #具名元祖不能够重新赋值，attributeError错误
print(one.age)

kong=info('null',0,'')
print(info._fields) #打印具名元祖的各个字段
r=kong._replace(tel="3")  #replace替换， 传参字段和值，替换产生一个新的具名元祖
print(kong,r)






'''
使用 具名元祖的函数，传入参 *
'''

banji=[["李四",12,119],["王五",18,120],["赵六",22,121],["田七",17,114]]
for i in banji:

      a=info(*i)
      print(a,a.name,a.age,a.tel)


''' make方法： 传入与具名元祖长度相同的一个元素，进行返回一个具名元祖
     可以用来代替   与通过*不定长参数结果类似
'''
for i  in banji:
      mk=info._make(i)
      print(mk)