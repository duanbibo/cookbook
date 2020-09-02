import  pandas as pd

'''
pandas是基于Numpy的一种工具，是为了解决数据分析任务而创建的。Pandas纳入了大量库和一些标准的数据模型，提供了高效的操作大型数据集所需的工具


'''

#print(pd.test())

ex=pd.read_excel(r'')
print(ex.keys())     # 打印表头
print(ex[1:2].values,"打印单行数据")
