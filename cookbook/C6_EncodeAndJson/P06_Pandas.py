import pandas as pd
import numpy as np


'''
padas库支持读取与存取像csv、excel、json、html、pickle等格式的资料 HDF5
pandas是字典形式，基于numpy创建，让numpy为中心的应用变得更加简单。
  https://blog.csdn.net/LZH_12345/article/details/79798787
  
  pandas 核心概念：
        column =列名，表头字段
        index 索引 ，行。默认0-(N-1)
  
'''

'''
pandas数据结构
1.Series  一维数组 ，字符串表现形式：索引在左边，值在右边。如果没有为数据指定索引，会自动创建一个0-(N-1)的整数索引
               可以通过对象的value和index属性获取数组表现形式
2.DataFrame 表格型数据结构，包含一组有序的列
             dict={ 'name':[ ... ], age:[...],addr:[...]}
             pd.DataFrame(dict ,[index=[0..len(dict)-1],columns=dict.keys()])
            关键参数 data，  colums表头的字段，  index 每一行数据的索引
             获取列数据时直接通过返回的对应，调用对应的字段名称就可以了 对象.name.values
             获取行数据需要通过index， 对象.ix[ index] ,
             打印多行，多列时可以借助numpy的索引切片方法直接打印多行，
'''
s=pd.Series([1,2,3,np.nan,5,6])
print(s)
print(s[0],s.values,s.index ,"打印一维数组的索引和值")

#指定索引
zimu=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(zimu)


#通过numpy对象建立矩阵  6*4 6行4列  columns设置表头
dates=pd.date_range('20180310',periods=6)
#df=pd.DataFrame(np.random.randint(6,4),columns=['A','B','C','D'])
#print(df)

'''
创建表格类型的数据
'''
data={'names':['Bob','Jane','Jack','Ann'],
       'sex':['M','F','M','F'],
       'age':[21,30,26,28]}
#字典的键会作为表头的字段名
datef=pd.DataFrame(data)
print(datef)
print(datef['names'].values,"通过字典方式获取列名对应的value获取一列数据")
print(datef.age.values,"通过列名的属性方式获取一列数据")
#获取行数据就必须用到index了，可以调用的方法有iloc[index],
#  如果index为字符非数组时，使用loc['index']
# 使用 .ix[2]  .ix['b']  方法时前面两种的混合， 这个方法被弃用了
print(datef.iloc[2] ,"获取单行数据")
print(datef[0:2],"支持numpy的矩阵类型的切片打印多行")
#print(datef.ix[:,0:2],"打印多列")
print(datef['age'].min()) #获取某个字段的最小值的
print(datef.head(1))  #打印头几行
print(datef.append(['zs','M',23]))#增加一行数据
print(datef)


'''
读取excel等资源
'''
ex=pd.read_excel(r'患者注册绑定.xlsx')
print(ex.keys())
print(ex[1:2].values,"打印单行数据")



'''
多个DataFrame 合并
1.axis合并：    axis=0 表示竖向合并行增加，axis=1代表横向合并列扩展， 重置序列index index变为0 1 2 3 4 5 6 7 8
      pd.concat([df1, df2, df3], axis=0, ignore_index=True)
2.join 合并： 两个列和行不相等的矩阵进行合并的策略
   res=pd.concat([df1,df2],axis=1,join='outer')#行往外进行合并 ,没有的补充NaN，取和
   res=pd.concat([df1,df2],axis=1,join='inner')#行相同的进行合并 ,取交集
   res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])#以df1的序列进行合并 df2中没有的序列NaN值填充
      
       
'''
