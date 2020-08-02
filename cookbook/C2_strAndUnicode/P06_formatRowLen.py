import  textwrap
import os

'''
背景：当有一些很长的字符串，想讲他们重新格式化，使得它们能按照用户指定的每行多少来进行换行


   主要用于打印方面，设置终端输出样式
    
textwrap.fill( str ,每行的字符数量，)
  内部的策略：当输出文字是一个整体的时候，是到下一行展示还是在这一行展示？
             所以有额外的参数来控制
             initial_indent=''  设置到下一行展示，本行空起来部分    【 最佳】
             subsequent_indent= ''  设置在本行展示，可能会超过设置的宽度

'''
#print(os.get_terminal_size().columns) 获取控制台的列宽，支持多少个字符空间

''' 使用字符串的center,ljust 进行居中，靠左对齐等方式'''
st='Look into my eyes,look into myesys, the eyes, the eyes,the eyes,the eyes'
stduiqi=st.center(8,"=")
print(stduiqi,"每行设置80个如果不够进行填充其他字符字符满足80个字，"
              "如果实际字符长度超过控制的长度就无效，不影响字符串输出")

print("第一种不加策略，会将单词截取")
print(textwrap.fill(st,15,initial_indent=''))

''' 使用textwrap包控制每行的长度：每行5个字符长度，超过的话 换行展示'''
print("使用策略，第一种最少，满足不超过控制的前提下，将整个单词不和换行")
print(textwrap.fill(st,15,initial_indent=''))

print("第二种策略可以超过")
print(textwrap.fill(st,15,subsequent_indent=''))
