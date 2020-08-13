from fnmatch import fnmatch,fnmatchcase   #正则匹配文件

import posixpath

import shutil      #文件内容的复制
import  pathlib    #文件的面向对象的方法操作
import glob        #路径下批量匹配文件， 也可以遍历路径下的目录
import linecache   #读文件的缓存

'''
对于名称进行匹配，利用shell匹配通配符

 fnmatch :是一个返回为布尔值的一个函数，第一个是给定的字符串，第二个是匹配的样式支持正则表达式,
   只支持单个匹配，所以说如果有批量的话，必须遍历后进行逐个匹配。或者利用推导式进行
     name for name in names if fnmatch(name, 'Dat*.csv')
 fnmatchcase:是区分大小写的匹配。如果给定的字符串是大小，匹配的名称为小写，返回为False   
  
'''
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('Dat45.txt','Dat[0-9]*'))

import os

print(os.path)
print(os.path.basename(__file__),"os.path.basename打印文件名称和后缀")



''' 
 使用pathlib 进行路径、文件属性、文件内容操作 ：它是基于面向对象的，
 1.对于路径的拼接方面，可以直接使用/ +文件名的字符串 , 避免了os.path库的os.path.join(目录，路径)
 2.对应文件的读写，不需要open函数，直接可以 read_text() 返回文件内容，其实内置了open的 read()函数，并且使用了with语句
 
'''
import pathlib
import  os
import copy


data_foler=pathlib.Path("C:\\Users\87842\Desktop\Work\python\cookbook\source")

file_to_open=data_foler/"test.txt"
print("这是使用pathlib的库操作路径，",file_to_open)
print(file_to_open.read_text())

print(file_to_open.name,"打印文件名+类型")
print(file_to_open.suffix,"打印文件名后缀即扩展名")
print(file_to_open.stem,"打印文件仅限名称")
newname="somefile.txt"

''' 使用 os.path内的 split 和join方法，
              将路径切割，返回2个元素的列表以最后一个斜杠为分隔符 
               ；将目录和文件名拼接，'''
cur=os.path.split(__file__)
print("当前文件目录", cur)
osfile=os.path.join(cur[0],"somefile.txt.txt")
print(osfile)


   #rename : 如果是路径效果和replace一样 文件重命名，带上扩展名
p=pathlib.Path("C:/Users/87842/Desktop/Work/python/cookbook/cookbook/huan")

#p.rename("C:/Users/87842/Desktop/Work/python/cookbook/cookbook/C2_strAndUnicode/2")
#print(p)
#p.replace("C:/Users/87842/Desktop/Work/python/cookbook/cookbook/C2_strAndUnicode")
#repalce 必须为文件名




all=data_foler.match("cookbook")  #文件名是否与后面的正则匹配



''' 匹配目录下所有的文件,不会递归进行的'''
pipei=data_foler.glob("*.py")
#print(list(pipei))
allpipei=data_foler.glob("**/*.py")  #在正则前面加上 **/就能递归匹配了
#print(list(allpipei))
rg=data_foler.rglob("*")
print(list(rg))
print("rglob :递归遍历所有类型的文件")

''' 遍历目录下的所有文件'''
#还是上面那个rglob方法，正则匹配写上*就可以


''' 匹配文件名，还是用glob模块进行'''

li=glob.glob(os.path.split(__file__)[0]+'/*.py')
print(li,"glob库")



''' 这个glob库，专门做文件名的匹配,它匹配的结果默认返回列表'''

list1=glob.glob("[A-Z][0-9]*.py")
print(list1)

'''
文件内容复制
'''

import shutil

shutil.copy('C:/Users/87842/Desktop/Work/python/cookbook/cookbook/C2_strAndUnicode/2','3.txt')


'''
文件读缓存
'''
import linecache



'''exec执行'''

#  execfile（文件名，全局，本地人）   execfile() 函数可以用来执行一个文件。
# 在python 2存在。在python3 有exec()函数执行
#exec（编译（打开（文件名，rb） ）.read（），文件name，'e​​xec'），globals，locals）
#exec 是没有返回值的
exec(open(r'H://test.txt','r').read())