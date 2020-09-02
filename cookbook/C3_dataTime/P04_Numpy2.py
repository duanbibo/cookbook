import  numpy
import numpy.matlib    #矩阵库
import numpy.linalg    #线性代数的库
from  matplotlib import pyplot as plt  #绘图工具



'''
矩阵和线性代数的计算 :排序 、搜索、计算函数

'''

#shape: 形状  ，reshape 重新调整大小

#产生一个矩阵，4行6列，每行6个元素
jz=numpy.arange(24).reshape(4,6)
print(jz)
print(jz.ndim)
print(type(jz),"接下来要对矩阵进行转置，行列点到")

# .T方法 ：将行与列进行转换
print(jz.T)

'''
 NumPy库提供了各种排序功能。这些排序函数实现了不同的排序算法。每个排序算法的执行速度、最坏情况下的性能、所需的工作空间和算法的稳定性各不相同。
  sort ：原地排序
  
'''
numpy.sort(jz)
print(jz)

 # 传入一个矩阵结构，返回一个新的矩阵,矩阵的值会填入随机数
newjzhen=numpy.matlib.empty((2,2))
print(newjzhen)

'''
线性代数：两个矩阵的计算 等方法 。
       numpy.matmul 两个矩阵的点积，
'''

