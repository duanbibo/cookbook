import numpy

'''
对大型数据集比如数组进行计算，它要比math模块计算快上倍，因为内部使用的是数组，在系统内存是连续的

Numpy 库，提供了一个N维数组类型ndarray,用于描述相同类型的“元素”的集合，我们可以使用N个整数来对元素进行索引。
在NumPy库中，所有ndarrays都是同质的：每个元素占用相同大小的内存块，并且所有块都以完全相同的方式解释
除了基本类型（整数、浮点等）之外，数据类型对象也可以表示数据结构

  创建多维数组很多方法： 创建后返回的实例为 ndarray
         numpy.array(object,[dtype,copy,order,subok,ndmin]) 传入一个多维数组，
               arange(start,stop.stemp.dtype) ,在给定间隔内返回均匀间隔的值
               copy(a,[,order]) 返回给定对象数组的副本
               full(shape,fill_value,[dtype,order,subok])
               
  核心变量说明：             
  numpy.shape  :打印多维数组的结构。返回一个元祖（行，列）
  numpy.dtype  : 打印多维数组的元素类型  
  order        :排序用到的关键词 
  ndarray      :创建数组返回的实例类型
 
'''

#需求，对列表的每个元素的值进行乘以2
x=[1,2,3,4,5]
print(x*2,"显然这种是错误的，这样只是对列表内容的复制")

x2=[]
for i in x :
      i*=2
      x2.append(i)
print(x2,"调用for循环遍历后使用*=直接赋值，再外部声明个空列表，append进去")



an=numpy.array(x)
print(an*2,"使用numpy模块，对数组的每个元素都进行乘以2操作")
print(an+4,"对每个数组的元素进行加值")

bn=numpy.array([5,4,3,2,1])
print(an-bn, "两个数组相运算，下标对下标进行运算")

'''

多维数组的运用：扩充python列表的索引功能，在打印指定行的基础上，能够打印列，以及指定数组的区域，或者单个元素 
   语法：[  行，列]  它会对表达式进行解析，内容其实还是下标
       如果行，列是一个区间范围的话(即在内部再使用切片)而非单个元素，它会打印组成的区域

             用法[:,n] 对多维数组打印指定的n列。n指的还是索引。 逗号前代表start:end  ,使用冒号占位，代表所有的行
             打印指定的区域  [1:4,0,3]  打印多维数组的2,3,4行的第1,2,3个元祖组成的数组
             
'''
#构造数组方法一，通过array方法传入数组，默认所有元素类型为int类型
duo=numpy.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

print(duo[0],"打印多维数组第一行")
print(duo[0:2],"使用多维数组打印第1，2行")

print(duo[:,0]," :,target 打印多维数组第一列")
print(duo[:,0:3],":, start:end  打印1-3列")

print(duo[2,2],"试着打印第3行第三个元素")
print(duo[0:2,0:2],"打印指定区间范围")
print(duo[1:4,0:3],"-----[1:4,0,3]  打印多维数组的2,3,4行的第1,2,3个元祖组成的数组")

'''对指定区域范围内重新赋值，是在原有的基础上改变的'''
duo[1:4,0:3]+=10
print(duo)





'''对多维数组更改值，逻辑判断,相当于三元运算， 对每个元素进行判断，如果小于10，。。。 否则 XX

'''

print(numpy.where(duo<10,duo,10),"where 语句，如果小于10不变，大于10的话改为10")
print(numpy.where(duo<10,duo,duo-10),"如果小于10的话不变，大于10的话-10")


'''
数组操作函数：除了上面的类似切片的方式返回一个数组之外，还提供一些API用来对数组的增删改查
    ndarray,fill(value)：对数组使用值进行填充
    ndarray.reshape(shape,[,order]):对数组重新变换结构如 4*4 转换为 2*8 ,转换后必须保证数组内所有元素刚好占满
    ndarray.ravel() 返回展平的数组
    ndarray.repeat(repeat[,axis]):重复数组的元素
    ndarray.choose(chooices,[,out,mode])
           .sort(order=)    .对数组进行就地排序


'''

#item方法只能提取单个元素
print(duo)
print(duo.item(3,3))

#把多维数组转化为嵌套的list
duotolist=duo.tolist()
print(duotolist)


'''
构造多维数组，自定义类型

'''


dt=numpy.dtype([('name','S10'),('age',int)])
info=numpy.array([("raju",21),("anik",25)],dtype=dt)
print(info,"下面将对多维数组每行排序，指定定义的数据类型")
print(numpy.sort(info,order='name'))

print("----------------------")
aint=numpy.array([[1,2],[3,4]])
print(aint.dtype)              #打印多维数组的元素类型
astr=numpy.array([[4,3],[2,'1']])      #当数组内的元素有int类型也有str类型时，会考虑将转换为str
print(astr.shape)

empty=numpy.empty((2,3))  #通过结构创建数组,值是随机数
print(empty)
full=numpy.full((4,4),0)  #通过full创建数组，指定填充的值
print(full)
re=full.reshape((2,8))  #对数组进行重新设计结构
print(re)

#自定义数组，相当于
