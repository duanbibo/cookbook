import fileinput

'''
对标准输入或多个文件进行逐行遍历，相比open方法批量处理文件，它可以对文件、行号进行一定的控制
默认是不修改源文件的。可以添加 inplace=True ,直接修改源文件

fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)

创建并返回一个FileInput类的实例。files指定要处理的文件，可以是一个多元元组，表示按顺序批量处理元组内文件。
inplace参数最关键，可设置是否对源文件进行修改；backup则用于指定对源文件进行备份的后缀名；
mode用于指定文件读写方式，和open()方法的定义一样， 默认为只读‘r’。

同样的，fileinput.input()方法也可以作为一个上下文管理器使用，返回文件的句柄

api: 
        
   fileinput.filename()    :返回当前正在处理的文件名
   fileinput.fileno() 当前文件的行数
   fileinput.lineno() 返回多个文件的行数

'''
with fileinput.input(files=("H://三国杀/log.txt","H://三国杀/kongtt.txt"))as f:
       print(f)

       for  line in f :
            line=line.rstrip()
            num=fileinput.lineno()

            print("#%d\t%s" % (num, line))


print("============使用withopen读，根据句柄直接循环遍历每行数据")
with open('h://三国杀/log.txt','r')as f:
      print(f)
      #第一种使用句柄的read方法，将内容一次全部打印出来，如果文件大，内存吃不消
      str=f.read()
      print(str)
      #第二种:直接遍历句柄，调用for循环的生成器，一次在内存中读取一行数据。
      # for i in f:
      #       print(i)

print("使用open函数，试一下，他也支持根据获取的文件句柄直接用for循环的生成器一行一行的读")
o=open('h://三国杀/log.txt','r')
for i in o:
      print(i)