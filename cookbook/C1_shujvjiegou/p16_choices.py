'''
筛选
'''
'''
筛选时使用filter ，filter采用返回值为True 或Fals 进行判断，
        第一个参数为函数表达式返回值为布尔类型，第二个为可迭代对象
        
        #直接使用列表推导式，if语句写入后面


'''
la=[1,3,-8,4,-23,49]

fl=[i for i in  la if i>0]

print(fl)

f=filter(lambda a:a>0,la)
print(list(f))

from itertools import filterfalse
'''
迭代工作类库，提供了一个filterfalse的函数，提供相反的结果
'''
ff=filterfalse(lambda a:a>0,la)
print(list(ff))



'''
compress :构建筛选结果。 
      compress函数根据第二个参数的布尔值类型确认是否要加入构建后的生成器
      第一个是源数据可迭代对象，第二个参数是源数据每个值对应的布尔值类型
      比较麻烦


'''
from  itertools import  compress
more0=[n>0 for n in la]
print(more0)   #使用列表推导式，输出true或false的结果
c=compress(la,more0)
print(list(c))

