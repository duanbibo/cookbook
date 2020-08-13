import re

'''

字符串分割： str的只支持单个分割。 re正则的split支持
'''

'''
使用字符串的split进行切片分割只能做些简单的操作，可以考虑使用正则表达式的split方法
当进行分割的字符串前后出现了空格时，无法进行直接的剔除，
    必须再for循环遍历下调用字符串的strp方法清除前后指定的字符串
'''

line="das,fdsf;   f——s_df;fsdfsd;dasd:6456 345 7 "
print(line,"原始字符串")
ll=line.split(";")
print(ll,"使用字符串的split方法对一个元素只能指定一个分隔符")
lkong=[]
for i in ll:
      c=i.strip(' ')
      #print(c)
      lkong.append(c)
print(lkong,"使用字符的strp进行清除每个元素的前后空格")


r=re.split(r'[;,:\s]+',line)  #中括号内的元素之间的关系是or的关系，还是代表一次匹配
#\s代表空格、换行、回车、换页、制表
print(r,"使用正则表达式可以使用多个分隔符，只要在中括号内符合【逗号分号\s空格】")


''' 使用字符串的 splitlines 将字符串进行切片，每行放在一个页表的元素
         其中一个布尔值的参数 keepends 是否在列表元素显示 \n 换行字符，默认为False
'''
text1='''       多行文本
进行切片'''
duohang=text1.splitlines()
print(duohang )


'''  读取文件的read  和readlines
   read:返回的是一个字符串，按照文件进行换行。  带参数读取文件多少额字符串，如输出数组大于该行的实际长度，接着读下一行
   readline:返回字符串，不带参数只读取一行的数据，带参数按照字符读取仅读取当前行的字符串。如输入3 只读取前3个字符
   readlines:读取全部内容，带的参数指的是字符串。而非行号
   
    读取后字符串后面含有\n 时，怎么去除
    1. 使用read()返回文件全部内容不带\n的字符串后，在使用splitlines方法，按照字符串的行进行切片  
    
    2. 使用Readlines读取后返回一个列表，对列表内的元素进行rstrip('\n')
    
      第2种方式的误区:
        直接用Readlines后返回的是一个列表，无法对列表的元素直接调用字符串的rstrp,
         由于字符串不支持原地修改，所以需要在for循环外部声明个列表将修改后的字符串append到这个列表内
         
    3. 使用Readlines读取全部后返回的是一个列表，将列表的每个元素调用join方法转化为字符串就可以了
           ''.join(list).strip('\n') ，最终在通过其他方法转换为list .不推荐使用
    
            
'''

with open(r'../../cookbook/somefile.txt') as f:
     ''' 最佳方案去除\n'''
     data=f.read().splitlines()
     print(data,"最佳方案", end='\n')




''' 使用正则和字符串的方法，做切片、匹配、替换等。'''
inde=line.find('df')
print(inde,"通过字符串的find方法查找对应元素开始的下标,他的查找是惰性的，查找不到返回-1")

en=line.index('df')
print(en,"index 方法也能返回元素的下标，查找不到会报错")

rtatil=re.search(r'^\w{3}',line)
print(rtatil.group())

print(re.match('\w{3}',line),"math的返回结果只要不为None就代表匹配成功了")
print(line.startswith("das"))