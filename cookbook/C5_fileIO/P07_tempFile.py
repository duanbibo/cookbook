import tempfile
from tempfile import TemporaryFile
import time

'''
当程序运行中，我们需要创建临时文件或目录以便使用，在这之后我们希望将这些文件销毁掉，
  临时文件会默认放在系统内的Temp 目录下，自己也可以指定目录，临时目录文件的名称是系统产生的，
   临时文件的名称是系统产生的，没有后缀名.自己可以传入 
    prefix =文件前缀名  suffix =文件扩展名，delete=产生文件使用后是否回收，dir=临时文件的存放目录
    来自定义临时文件的具体属性
   参数只需要指明读写模式

 使用上下文管理，在exit之后就已经销毁，或者调用 对象的close()方法
  自己可以在函数内通过delete=False, 设置不进行回收销毁
  使用
'''
#临时文件设置 具体的属性
with TemporaryFile('w+t' ,dir=r'H://',prefix='pythoncookbook' ,suffix='.txt',delete=False) as f:
      f.write(" temp File \n")
      f.write(" 第二行 \n")
      f.seek(0)

      data=f.read()
      print(data)


print(tempfile.gettempdir(),"找出系统存放临时文件的目录")