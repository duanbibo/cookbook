#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
字典的key和value的计算，利用max ,min 这类生成器函数。
他们都支持 一个关键字key,可以与lamdba函数一起工作，可以直接根据他们的key进行排序等操作
'''


prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
'''需求：将字典的key和value进行转换
    实现方式：遍历字典的key和value，利用zip函数进行组合，组合后放入dict工厂函数内。产生新的dict
'''
fanzhuan=dict(zip(prices.values(),prices.keys()))
print(fanzhuan)

'''
需求：求出字典中value值最大的key,
         核心：利用max()函数，第一个放遍历的value，第二个放遍历的key，然后zip组合。放入max函数中。
              求出组合出来的一组数据，然后利用获取的zip对象根据对象的下标第二个是key,获取key值
        

'''

mk=max(zip(prices.values(),prices.keys()))
print(mk,mk[1])


'''错误方式：不能使用key
        mk=max(prices,key=lambda s:s.keys())
        字典是无法通过key的func进行常规遍历的。 not callable  
         需要用【】方式     mk=max(prices,key=lambda s:s[k])    根据value值进行排序
        '''

''' 这种方式：使用字典的items返回一个类似于元祖的对象，对着对象可以调用下标，可以指定key或者value排序'''
print(type(prices.items()))

s=sorted(prices.items(),key=lambda item:item[1])
print(s)
