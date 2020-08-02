

'''
字符串格式化的几种方式
1.  %   %s 字母 %d数字 %f 浮点型 %c ascii码
2. .format(序列)
3.      format_map(字典)

'''

li=[1,2,3]
dict1={'key1':3,'key2':4}
print('%s ,%d ,%.2f' %('1',4,23),"使用%")
print('{},{}'.format(1,2),"使用format传入序列，在格式化前面可以通过{} 来替换")
print('{1}，{0}'.format(*li),"使用format时仍可以在字符串里面使用下标，自定义格式化输出位置{1}，如果format内是一个列表对象，"
                            "那么在格式化的时候需要加上* ，自动解包，否则它会单独放在第一个大括号内")

print('{key1},{key2}'.format_map(dict1),"使用format_map传入一个字典。前面字符串里面用大括号写上{key}的值")

print(" format_map( dict) 可以用来做文本插值，类似于模板语法的{{}}，直接进行解析")

'''
字符串拼接
'''
str1='ab4'
pinjie='.'.join(str1)
print(pinjie,"使用join方法将可迭代对象与字符串进行拼接")

''' 将列表转化为字符串'''
lts=','.join(str(i) for i in li)
print(lts  ,"将列表的元素转化为字符串")
print(li)
print('{},{},{}'.format(*li))

'''              
                 文本插值
1.使用format_map 传入字典，使用时在字符串{key}值进行替换
2.补充前提：vars() 函数或者 globals()函数收集字典 ,它能自动收集当前执行类的所有变量
3.结合使用format_map和 vars()函数,  '{attr1}{attr2}'.format_map(vars(instance))
  将传入实例化的值解析给 前面的字符串，前面的字符串必须也
  
  弊端：fomat() 和format_map()缺点就是没法优雅的处理缺少某个值的情况。即前面解析的字符串，在后面传值里面找不到
     避免这种情况，就是单独定义一个带有__missing__方法的字典类型
   
'''
name='a'
n=37
s='{name} has {n}  messages'
print(vars(),"vars()函数能够收集一个字典包括执行当前文件所有的内容")
print(s.format_map(vars()))

print(globals(),)
print(s.format_map(globals()))
#print(dir()) 返回列表属性集合，所有的方法

class person:

      def __init__(self,name,age):
            self.name=name
            self.age=age

p=person('田七',23)
print('{name} has {age} age'.format_map(vars(p)))

'''              自定义个函数/方法，能够解析文本插值，不需要进入传入format_map内的值，
           思路：1.在内部必须要调用执行方法的命名空间内的字典信息
                2.对于给定的文本插值，如果不存在在字典的中，进行不报错处理。比如不解析。
                
           选型：1.基础数据结构选择用字典。
                2.defaultdict中，有一个特有的魔法方法__missing__ ,当值不存在时，可以返回一个字符串。
                  所以定义的这个类，可以内部实现这个方法     
                
可能会出现的样式： 正常     ’{name} is {age} age‘ 解析 =>     张三  is 25 age
                  value值为空                                   张三  is   age
                   value值不存在                                 张三 is {age}  age 
                                      
                    字符串为空                   张三  is None  age       
 '''

class  sub(dict):
      ''' 这个类继承于字典，重写字典的missing方法，如果找不到key值return结果'''

      def __missing__(self, key):
             return  '{'+key+'}'




print('{name}is {age}age {don/t}'.format_map(sub(vars())))

''' 使用字典的setdefault方法来实现
 内部原理：""" D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
            先判断key是否在字典内，如果不在字典内，set['key']=value 赋值，赋值后在获取这个值。
         setdefault方法其实是一个get方法，获取指定键的值。
                   如果key不存在的话，就使用第二个参数；
                   如果key存在的话，第二个参数就不起作用
          
 '''

sud={'key1':1,'key2':2}
su=sub(sud)
v=sud.setdefault('key1','11')
print(v)

v=sud.setdefault('key3','3')
print(v)














