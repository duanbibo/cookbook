import re
import pyparsing


'''正则匹配分组  
  对一个字符串进行匹配时，正则提取的内容进行分组，然后根据组名打印出对应的分组名和值
  
  对于更高级的分词处理，可以用pyparsing模块和PLY这个包
   
'''
st="34324==ddd34234"

#创建正则表达式对象
D=r'(?P<Num>\d+)'
W=r'(?P<Str>\w+)'


'''编译单个分组，'''
d=re.compile(D)
g=d.match(st)
print(g,g.lastgroup,g.lastindex,g.group())



'''             一个正则表达式中多个分组:

每个分组需要单独使用小括号包括 :
             group() 如果不传参的话，默认将匹配到的正则进行犯规
             groups() ,返回所有的分组。包括二部分，总的正则匹配到的数据，各个分组匹配到的数据
             group('<name>'),传入指定分组名称，返回分组匹配到的多个数据
             
'''

two=r'((?P<yi>\d{5}).{2}(?P<er>\w{3}))'
res=re.search(two,st)
print(res.group(),res.groups(),res.group('yi'),res.group('er'))



''' 使用管道，将多个正则表达式进行合起来。只要匹配到任何一个就可以'''
master_str="|".join([D,W])
print(master_str)
master_pat=re.compile(master_str)
fd=master_pat.search(st)
print(fd.lastgroup,fd.lastindex,fd.group())

