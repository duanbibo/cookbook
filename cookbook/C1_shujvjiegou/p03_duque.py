from collections import  deque

'''

  

collections的duque队列中有一个参数为maxlen,如果超过，就将前面的挤出队列
'''
d=deque(maxlen=5)
all=dir(d)
#获取对象中的方法，将魔法方法给取出
func=[]
for i in all:
    if not i.startswith("_"):
            func.append(i)
print(func)

list="012345678"
for i in list:
      d.extend(i)
print(d)



'''
对文件内容进行逐一匹配，发现有匹配时，就输出当前的匹配行以及最后检查过的N行文本
'''

def search(lines,pattern,history):
      previrous_line=deque(maxlen=history)
      for li in lines:             #获取文件对象进行遍历，遍历后的单个元素为单行字符串。
            if pattern in li:       #在多行的列表元素中用in contain仓查找，如果符合的获取
                  yield  li ,previrous_line
            previrous_line.append(li)

# if __name__ == '__main__':
#     with open(r'../../cookbook/somefile.txt') as f:
#         for line, prevlines in search(f, 'Python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-' * 20)