import fileinput

'''
使用fileinput默认是不修改源文件的,主要作用是提供文件的读取，并且能够提供索引的行号
可以通过修改源文件的方式，对文件内容值的修改，可以对修改的文件进行备份


  把原文件的内容放在备份中变成新文件，然后在现有的文件中修改
  修改时，利用字符串的方法可以进行修改

'''
filename='inputfile.txt'
for line in fileinput.input(files=filename,inplace=2,backup='.bak'):
      line=line.replace('root','Root')
      print(line)


