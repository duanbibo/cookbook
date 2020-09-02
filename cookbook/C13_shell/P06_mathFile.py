import fnmatch
import os


path=os.path.split(__file__)[0]
print(path)


# 匹配文件返回布尔值，第一个参数是文件名，第二个参数是正则表达式
pp=fnmatch.fnmatch(__file__,'*.py')
print(pp)

#遍历文件目录，递归遍历,产生的数据是一个元祖：
# 第一个为当前遍历的目录路径，
# 第二个是当前目录下的目录名列表，
# 第三个是当前目录下的文件名。
lpath=os.walk(os.path.split(__file__)[0])
print(list(lpath))


import  glob
import pathlib #

'''
递归： 1.   os.path.walk            递归遍历
       2.  glob(FILENAME正则)               可以递归，传入的参数是一个正则表达式组成的路径，返回符合的结果，路径里面可以用*匹配
       3.     pathlib.glob/rglob    
             可以递归    首先利用pathlib.Path('路径')返回一个文件路径，利用这个文件路径调用glob方法，传入正则表达式，返回符合的结果
       4.     fnmath   借助遍历os.listdir()返回的文件夹名称和文件，循环判断每个文件类型，在做遍历.
                不推荐。因为返回的结果不带路径，只是个文件名，无法通过调用os.path.isXX(path)
 四种方式都可以
'''
print("递归的几种方式")

path=r"C:\\Users\87842\Desktop\Work\python\cookbook"
print("os.walk")
#print(list(os.walk(path)))

gl=glob.glob('C:\\Users\87842\Desktop\Work\python\cookbook\*\*')
#print(gl)



p=pathlib.Path("C:\\Users\87842\Desktop\Work\python\cookbook")
pglob=p.glob('*.*')
print(list(pglob))

'''list dir 遍历返回当前内的所有文件包括目录'''
opath=os.listdir(os.path.split(__file__)[0])
print(opath,"返回文件")

