
import re
'''
不区分大小写，对于字符串而言有特定的方法，upcase ；
对于正则而言，每个匹配的时候都有一项参数值，用来不区分大写偶写  flags=re.IGNORECASE 
                                              换样匹配  ：flags=re.DOTALL
'''
str="sASA444"

su=str.upper()
ru=re.search(r'sasa',str,flags=re.IGNORECASE)
print(su,ru.group())



''' 字符串对齐 每行支持多少个长度 不过不够的话左右或者两边补齐，【如果不够的话，填充字符;超出的话，不会被限制】
           ljust center  rjust  :左对齐不够右边填充 
'''
nstr="hello word"
zuoduiqi=nstr.center(20,"=")
print(zuoduiqi,"左对齐，每行20个元素，如果不够的话，向右边填充指定字符")