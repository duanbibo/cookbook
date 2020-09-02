from functools import partial   #冻结参数

'''
冻结参数的目的：减少实际传入的参数。
partial :主要是冻结参数，固定将原函数以及提供额外的参数，组合成一个新的func,
       每次调用这个组合后的func时，默认先执行原函数和冻结的参数
        语法    partial(oldfunc  , parameter)
        
    冻结参数常常可用来调整其他库中用到的回调函数的参数签名，如异步执行结果
    func:执行的函数
     funresult: 回调的函数
    a.apply_async( func, func_param,callback=partial(funresult,param)):
     result=func(*func_param)
     callback(result)  
    
      
'''

def su(a,b,c):

      return a,b,c

print(su(1,2,3))

#将原有的一个或者多个参数进行冻结，按照冻结函数传入的值传入
psu=partial(su,b=4)
print(psu(a=1,c=2))

