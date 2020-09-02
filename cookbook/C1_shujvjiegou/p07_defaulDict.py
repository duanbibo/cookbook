from collections import defaultdict, Counter


'''
这个是工厂函数，  继承自dict 
 可以自定义构建 字典的value值类型，比如可以对字典的键进行add .append等操作
 
 
 class defaultdict(Dict[_KT, _VT], Generic[_KT, _VT]):
 
    default_factory = ...  # type: Optional[Callable[[], _VT]]   #工厂函数返回一个指定类型
   
    def __init__(self, default_factory: Optional[Callable[[], _VT]],
                 iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...   #通过init方法，传入工厂函数的类型
                 
                 

 工厂函数 defaultdict ,有一个特有的魔术方法 __missing__(self,e),
        用来给key赋一个默认的value，当key找不到时会输出这个值
 
'''
#设置工厂字典函数类型为list，他的value可以调用list内的方法，如append
dl=defaultdict(list)
dl['1'].append(1)
dl['1'].append(2)
print(dl)

#应用：求出字符串中的各个字符出现的频率  ,遍历字符串，当key出现相等的情况下对key对应的值进行+1,deaultdict:按照顺序打印

di=defaultdict(int)

str="zkdjashjkdhasjjkh"
for i in str:
      di[i]+=1
print(di)


#其他方法，来求字符串中出现的次数  利用counter ,counter中并且将出现的进行降序排列。出现多的排前面
c=Counter(str)
print(c)

print(list(c.elements()),"elements方法：打印counter的key值,不去重")
print(c.most_common(2),"most_common(X) ,返回当前对象前X位value值最大的，key值和对应value值")
print(c['w'],"当访问不存在的元素时，默认返回为0而不是抛出KeyError异常。")
print(c.update("cded"),"对counter对象调用update方法，增加元素")
print(c)
print(c.subtract("decc"),"对counter对象调用subtract方法，较少元素,减少后key不会消失，对应的value显示0")
print(c)

#原始笨方法:利用set 和list  ， 将可迭代对象转换为列表，后面需要列表的count方法统计出现的次数
# set 可迭代对象，做去重处理， 根据list.count( set中的每一个元素，)  求出当前元素在可迭代元素的数量
   # 首先通过for循环遍历整个set对象，根据set对象去重的元素去确定循环，外部使用个空的列表
   # 在for循环插入set当前的对象和通过count返回的数量插入空列表中

print("使用set，list 进行求字符串出现的次数")
lis=list(str)
print(lis)
slis=set(lis)
result=[]

for i in slis:
      result.append((i,lis.count(i)))
print(result)




#扩展：同理当value的类型为set时，可以调用set类型的去重


