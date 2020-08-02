import  re

'''

移除字符串中部分字符 ：如果他们不指定参数的话，默认去除空白字符
strip:从字符串开始和结尾去除字符
lstrip:从字符串左边去重字符
rstrip:从字符串右边去重字符
'''

str='                 hello word    '
nstr=str.strip()
print(nstr,"左右两边都去除空格了")
dstr=nstr.strip('d')
print(dstr," 去除word后面的d")



'''replace  :字符串替换 '''
rep=str.replace('ll','11')
print(rep,"遍历字符串，将字符串中的ll替换为 11")



'''
利用正则表达式替换字符串中的内容 ，可以单个字符串替换
'''
rstr=re.sub(r'^\s*','',str)
print(rstr, "利用正则表达式将特殊字符替换为空，去掉前后空格 ^\s  * :0或多次")




