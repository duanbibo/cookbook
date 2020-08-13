import  numpy
import numpy.matlib
import numpy.linalg    #线性代数的库



'''
矩阵和线性代数的计算
'''

#产生一个矩阵，4行6列，每行6个元素
jz=numpy.arange(24).reshape(4,6)
print(jz)
print(type(jz),"接下来要对矩阵进行转置，行列点到")
print(jz.T)


'''
线性代数：两个矩阵的计算 等方法 。
       numpy.matmul 两个矩阵的点积，
'''

