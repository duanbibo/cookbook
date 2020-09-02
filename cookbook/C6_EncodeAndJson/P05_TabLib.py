import tablib

import io

'''
作者：开发了requests库

使用第三方模块Tablib将数据导出为不同的格式，包括Excel， json,HTML,Yaml,CSV,TSV等格式

需要通过date=tablib.Dataset() 创建数据的实体类，同时调用这个实体类的append方法添加行数据，header方法设置表头
             data.dict()方法打印全部数据：对应的样式是字典类型每行数据与表头的每个字段组成键值对。
             

我们在对Dateset对象进行了一些列的操作，最终还是要保存在硬盘中(也就是文件)
这也是tablib的强大之处，你可以将Dateset对象转换为你想要的格式，保存下来。
导入时，利用的还是 文件对象的write方法，将data.数据类型写入就可以

 with   open( 'tablib.csv' ,'w') as f:
          f.write(data.csv)
 

'''

#在Tablib模块中，使用tab.Dataset可以创建一个简单的数据集对象实例。
data=tablib.Dataset()

names=[ '张 三','李 四']
for name in names:
      fname,lname=name.split()
      data.append([fname,lname])

#调用数据的字典方法获取数据信息
print(data.dict)

#可以在数据集中添加标题
data.headers=['First Name','Last Name']
print(data.dict)            #添加header后，获取的实例还是OrderedDict类型的数据

#为数据重新添加一列，指明添加列对应的字段，同时再为已存在的2条数据添加列中对应的值
data.append_col([20,22],header='Age')
print(data.dict) #此时打印时，header ，value，这种形式按行进行打印


#这里为啥必须用io.open导入？
with  io.open('tablib.json','w',encoding='utf-8')as f:
       f.write(data.json)

with io.open('tablib.csv','w',encoding='utf-8')as f:
      f.write(data.csv)

with io.open('tablib.yaml','w',encoding='utf-8')as f:
      f.write(data.yaml)

with io.open('tablib.xls','wb')as f:
      f.write(data.xls)

'''
进阶：在实际应用中，有时需要在表格中处理多个数据集，如将多个数据集导出到一个excel文件中，
    这个时候可以使用TabLib模块中的Databook实现。
    将创建的dataset对象，放入 databook内当做参数


'''
data1=tablib.Dataset()
data2=tablib.Dataset()
data1.title="sheet11"
data2.title="sheet22"

#这里在传入多个数据集时，必须把数据集放在一个元祖中
book=tablib.Databook((data1,data2))

with io.open('tablib2.xlsx','wb')as f:
      f.write(book.xls)