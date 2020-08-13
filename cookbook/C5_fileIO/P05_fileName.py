import os
import pathlib   #基于面向对象的path处理，获取文件名，后缀名,大小，权限，内容读取 以前更改
                  #和Linux的一些文件系统管理类似



'''判断文件是否存在'''
filepath=r'H://log.txt'

print(os.path.exists(filepath))

'''路径分割，返回一个列表 从.处分割'''
print(os.path.splitext(filepath))

path=pathlib.Path(filepath)
print(path.name,"获取文件的全部名称",os.path.basename(path))
#print(path.read_text())


'''
 os.listdir() 返回当前文件夹下的全部文件和目录
'''
mulu=r'h://'
print("打印目录下的全部文件和目录，不进行递归os.listdir")
print(os.listdir(mulu))
print("=------------=")



'''
 利用 fnmath 和glob遍历目录符合的文件名
'''
import fnmatch
import glob


'''
递归： os.path.walk            递归遍历
         glob                    利用正则，无法递归，只能当前文件夹
            pathlib.glob/rglob    可以递归    利用正则  /默认递归遍历
            fnmath   借助遍历os.listdir()返回的文件名称，循环判断每个文件
 三种方式都可以
'''

#print(list(os.walk(mulu)))
print(glob.glob('H://*.*'))
#print(list(pathlib.Path(mulu).rglob('*')))
#print(list(pathlib.Path(mulu).glob('**/*')))
