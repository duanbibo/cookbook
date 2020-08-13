import shutil

'''
shutil 是对OS模块的补充，主要针对文件的的拷贝、删除、移动和压缩、解压操作
'''

'''
shutil.copyfile :传入2个路径完成复制功能
'''

# t=shutil.copyfile(r'h://log.txt',r'h://log2.txt')
# print(t，"返回结果为目标目录")

'''
move 用于移动文件目录
'''
# m=shutil.move(r'h://log2.txt','h://三国杀/log.txt')
# print(m)
'''
copyfileobje:将第一个文件内容写入到第二个文件中，传入的必须是file对象，不能是文件路径。
                在第二个文件可以选择mode，进行追加还是覆盖
'''
result=shutil.copyfileobj(open(r'h://三国杀/log.txt'),open(r'h://三国杀/kongtt.txt',mode='a'))
print(result)  #返回结果为None

'''
copytree :递归复制，将目录下的文件复制到指定目录下
rmtree:递归删除
'''
# shutil.copytree()
# shutil.rmtree()