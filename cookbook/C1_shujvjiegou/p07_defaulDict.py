from collections import defaultdict, Counter


'''
这个是工厂函数，  继承自dict 
 可以自定义构建 字典的value值类型，比如可以对字典的键进行add .append等操作

 工厂函数 defaultdict ,有一个特有的魔术方法 __missing__(self,e),
        用来给key赋一个默认的value，当key找不到时会输出这个值
 
'''
#设置工厂字典函数类型为list，他的value可以调用list内的方法，如append
dl=defaultdict(list)
dl['1'].append(1)
dl['1'].append(2)
print(dl)

#应用：求出字符串中的各个字符出现的频率  ,遍历字符串，当key出现相等的情况下对key对应的值进行+1

di=defaultdict(int)
str="kdjashjkdhasjjkh"
for i in str:
      di[i]+=1
print(di)


#其他方法，来求字符串中出现的次数  利用counter ,counter中并且将出现的进行降序排列。出现多的排前面
c=Counter(str)
print(c)
for k,v in c.items():
      print(k,v ,end="...")



#扩展：同理当value的类型为set时，可以调用set类型的去重


