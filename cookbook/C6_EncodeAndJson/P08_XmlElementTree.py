
from urllib.request import  urlopen

import xml.dom.minidom
import xml.sax
from bs4 import BeautifulSoup  #解析HTML的，HTML的tag基本上都是预定义的
import lxml

from xml.etree import ElementTree as ET

'''


 
解析xml库： dom解析不推荐，他需要将xml文档全部加入到内存中 ，sax解析基于事件驱动的，虽不需要不全装入xml但是过程较为复杂
            推荐使用elementTree,是Cython的实现，速度快，消耗内存少，性能占优，支持xpath查询,
            并且支持将python的数据结构类型dict转换为xml数据结构dict_to_xml,转换为字典后，声明外部的
             解析时，必须是读取xml文件，不是是普通的str字符串
             
       s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
       字典转化xml时，需要一个最外层的一个tag包括字典内的各个属性，各个key当做子tag，value单做tag内的text
       <stock> 
        <price>490.1</price>
        <shares>100</shares>
        <name>GOOG</name>
       </stock>     
            
      xml结构 ：   tag   attrib    text 
           attrib是字典，每个属性都是一个key，可以利用字典的内置方法 items ,keys 
           text是标签内的值
           
           对于tag的查找使用find 和findall  。
      对于任意一个tag下面可能有多个节点，需要用list的for循环遍历。获取
            
    
            
'''

#传入文件件时获取整个xml的对象。
tree=ET.ElementTree(file='test.xml')
print(tree.getroot().tag,"打印根节点")

#如果一个节点下存在多个tag数组，就需要用iter方法迭代，通过tag进行查找
# for i in tree.iter(tag="food"):
#     ...
