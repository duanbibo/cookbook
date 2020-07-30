'''

找出两个字典中相同的键或相同的值


'''
'''
直接遍历key或者value，进行一元运算，- 求差值 ：第一个部分减去两者共有的
                                    &  求共同部分：
                               + 无法求和，因为  返回类型是set

 为什么可以直接比较？是不是和鸭子类型有关，只要同类型的就可以参与运算
             不是，字典的key ，是可以支持并、交、差 的运算
 
'''
a = {
      'x': 1,
      'y': 2,
      'z': 3
}

b = {
      'w': 10,
      'x': 11,
      'y': 2
}
k=a.keys()-b.keys()
print(k ,type(k),"两个字典相同的key")
kv=a.items()&b.items()
print(kv,type(kv),"两个字典相同kv")

'''
使用字典推导式
'''
dicta={'a':1,'b':2}
dt={ k:v  for k,v in dicta.items() }
print(dt)

'''字典内取出子集,取出字典中 value值大于80的数据'''
dictz={'zhangsan':45,'lisi':90,'wangwu':49,'zhaoliu':66}

dz={k:v for k,v in dictz.items() if v>60}
print(dz,"字典推导求字典中符合的value数据")

name={'wangwu'}
value=[66,90]

'''从字典里面找出，key是这个元素的键值对'''

kik={ k:v for k,v in dictz.items() if k in name}
print(kik,"字典推导求字典中在指定容器内的key")
kiv={k:v for k,v in dictz.items() if v in value}
print(kiv,"字典推导构建，值在指定容器中的 组")
