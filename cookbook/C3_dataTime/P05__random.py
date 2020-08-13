import  random



print(random.uniform(0,99),"随机值范围的小数")

value=[1,2,3,4,5]


#choice方法抽取值时，下次再抽取有可能会重复
for i in range(len(value)):...

print(random.choice(value))
print(random.choice(value))
print(random.choice(value))
print(random.choice(value))
print(random.choice(value))

#sample 依次返回多个值，多个值不会重复的
print(random.sample(value,3))

#洗牌算法，打乱重排
random.shuffle(value)
print(value)

#产生指定区间的随机数
print(random.randint(10,200))


#产生指定区间的随机数，并且要求步长
print(random.randrange(0,78,3))

#random.choies 在产生值时，可以设置权重。加权权重或者是比值权重



''''random.seed:设置初始的种子值，设置完后执行random相关方法后会记录本次的值
    当再出现seed时设置相同的种子参数，就会输出上次random产生的值
'''
#
#random的随机数其实是一个确定性算法，采用马特赛特旋转算法。
# 如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。

for i in range(5):
      random.seed(5)
      print(random.randint(0,10),"执行完毕后习")
random.seed(3)
print(random.random())
random.seed(2)
print(random.random())
random.seed(5)
print(random.random())



print(random.random())