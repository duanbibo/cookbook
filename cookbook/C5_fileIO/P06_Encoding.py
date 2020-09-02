import sys
import io

'''
io 包：为已经打开的文件流更改编码方式 


   利用io.TextIOWrapper   文本IO包装类
   
'''
print(sys.getdefaultencoding(),"获得系统的默认文件编码格式")
import urllib.request

u=urllib.request.urlopen('http://www.baidu.com')
f=io.TextIOWrapper(u,encoding='utf-8')
text=f.read()
#print(text)
f=open(r'H://log.txt','r')
print(f)
print(f.buffer,f.buffer.raw)