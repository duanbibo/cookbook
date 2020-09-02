import  csv

from collections import namedtuple
'''
 csv读取时，需要将文件的句柄传给reader方法
     csv.reader(fileobject,dialect=excel)
'''

'''
这里使用具名元祖进行解析数据，返回为类似于属性=值
'''
# info=namedtuple('info',['name','tel','weachat','pay'])
# with open(r'data.csv')as f:
#       f_csv=csv.reader(f)
#       for i in f_csv:
#             print(info(*i))
#

'''
利用seek 文件偏移，生成一个大文件     
                 1024   1KB           10241024 1MB  102410241024  1GB
                 可以通过   seek(10241024*n)   :从函数内部传入n来控制需要生成多大的文件
'''

with open(r'data.csv','wb')as csvfile:
       csvwriter=csv.writer(csvfile)
       csvwriter.writerow([])
