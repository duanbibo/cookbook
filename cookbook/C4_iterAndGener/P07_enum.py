
from itertools import chain
from collections import ChainMap

'''

使用枚举函数，将可迭代对象组合为类元祖，按照索引值
'''
'''
枚举类，默认是从0开始的，枚举的参数第一个为可迭代对象，第二个为枚举开始的地方，可以指定

enmerate(itear,start=0)
'''
my_list=["春天","夏天","秋天","冬天"]
for i in enumerate(my_list):
      print(i)


'''
结合实际情况使用，读文件内容，为文件内容增加行号,有点不好的就是枚举是从0开始的

'''
with open(r'H://三国杀/log.txt','r')as f:

      #第一种方式：验证文件对行切片，先返回字符串，在对字符串根据行号切，最终返回列表
      # str=f.read().splitlines()
      # print(str,type(str))

      #第二种方式：先返回一个列表，对列表的每个元素调用join方法，然后strip(\n) ,消除指定字符,返回字符串
      str2=f.readlines()
      t2=''.join(str2).strip('\n')
      print(t2,type(t2),"str")

      # print(f)
      # for i in enumerate(str,1):
      #       print(i)

'''试下字符串的splitlines'''

ddd='''这样才可以哦
  splitline方法必须使用多行文本,或者是文件IO输出的对线。
'''
ddd2="ddddd" \
     "ddddd2"
print(type(ddd))
q1=ddd.splitlines(keepends=False)
q2=ddd2.splitlines(keepends=False)
print(q1,q2)

''' 使用zip迭代多个序列'''
key1=(1,2,3,4)
value=['a','b','c','d']
z=zip(key1,value)
for i in z:
      print(i)

''' 使用chain将不同容器类型的可迭代对象放在一起'''

print("使用chain将不同容器类型的可迭代对象放在一起,如字典，字符串，列表，元祖，对字典迭代只能迭代出key")
t1=(1,2,3)
l1=[3,5,6]
c=chain(t1,l1)
for i in c:
      print(i)

print("当对字典容器放进去迭代时，只能迭代出key")
d1={'key1':'value1'}
d2={'key2':'value2'}

d=chain(d1,d2,t1)
for i  in d:
      print(i)


print("当使用字典类型时，无法将字典的value进行迭代查出来，使用集合工具类的chainmap可以将两个字典拼接")

cm=ChainMap(d1,d1)
print(cm)


''' 编写代码时，调用函数时，返回一个变量。这个变量就是return的结果集
      当这个函数被其他函数调用时，直接将变量传给其他函数当做实参。
       这是一种数据处理的管道，同时也是python的简洁之处，同事将代码简化拆分了。
        颗粒度更小了。使一个函数专注于做一件事。
        
     main: 
       a=funcA(x,y)
       b=funcB(a)
       c=funcC(z,i)  
       d=funcD(b,c)
       
'''

def su(a,b):
      return a+b

m=su(4,5)
print(m)
