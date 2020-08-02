import difflib
import linecache



'''
Difflib作为python的标准库，无需安装，作用是对比文本之间的差异，而且支持输出可读性比较强的HTML文档。

在Linux下，可以直接使用vimdiff命令比对文本，例如对a.txt与b.txt的差异，命令： vimdiff  a.txt  b.txt  即可。

 主要用在比较多行文本的数据 ，比如单个字符串比较无多大意义，且也没实际运行场景
 所以在比较时将文件加工成合适大小的片段。拿这个片段做对比

compare( a,b):

比较两个行序列，并生成delta（一系列行）。

每个序列必须包含以换行符结尾的单个单行字符串

‘-’字符  序列1独有的
‘+’字符   序列2独有的
‘ ’字符    两个序列共有的
‘？’         两个输入序列都不存在该行
'''


text1 = '''
text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
'''

text2 = '''
text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
'''

d = difflib.Differ()

diff= d.compare(text1.splitlines(),text2.splitlines())

print(list(diff))


print( "\n".join(list(diff)))


''' 利用difflib模块的 SequenceMatcher类中的 ratio ，返回他们的相似度

'''
s=difflib.SequenceMatcher(None,text1,text2)
print(s.ratio())


# print(diffsult)
# listsame=[]
# listduuo=[]
# listshao=[]
# for i in diffsult:
#       if i.startswith(' '):
#             listsame.append(i)
#       elif i.startswith('+'):
#             listduuo.append(i)
#       else:
#             listshao.append(i)
# print(listsame,listduuo,listshao)

