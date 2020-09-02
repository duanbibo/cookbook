from concurrent.futures import ThreadPoolExecutor ,as_completed
import time

'''
使用concurrent.futures库中的进程池或者现场池，构造函数有一个max_workers= 的参数，目的是创建进程池的大小，
池化技术避免了线程的初始化，销毁等消耗系统资源的操作。

通过返回的pool对象，可以在内部调用submit( func= , arg= ..)提交任务直接执行，避免了Thread类的start，同时
返回的是一个future对象，通过这个对象可以获取非阻塞的状态done()，以及result(),同时可以在线程执行完毕后增加回调函数
 future.add_done_callback(),回调函数中第一个参数要传入这个future对象



'''


def func1(c):
      print(time.time())
      time.sleep(c)
      print("func1休息了{}秒".format(c))
      return c

def func2(c):
      time.sleep(c)
      print("func2休息了{}秒".format(c))
      return " success"

def  huidiao(future):
      r=future.result()
      print(r,"回调函数执行中")
      return r

pool=ThreadPoolExecutor(max_workers=5)
#返回一个未来的实例
future=pool.submit(fn=func1,c=3)
#非阻塞的执行状态，是否完成,否
print(future.done())
#阻塞的result
print(future.result(),"result")
#回调函数
future.add_done_callback(fn=huidiao)

'''
单个函数多个参数，执行任务时，需要用到 zip( 参数化的可迭代对象，executor.map函数(函数名，参数化的可迭代对象))
 
  核心就是excecutor.map 将固定的参数名和可迭代对象进行一一调用
  
'''
import requests

def load_url(url):
      time.sleep(5)
      return requests.get(url)

print("---------------单个函数，多个参数，map执行：zip(迭代参数，map(函数，迭代参数))")

urs=["http://www.baidu.com","http://www.qq.com","http://www.sina.com.cn"]
with ThreadPoolExecutor(max_workers=3) as excecutor:
   for url ,data in zip(urs,excecutor.map(load_url,urs)):

     print( "执行结果；",(url,data.status_code))

'''
第二种方式，首先通过列表推导式返回一个生成器对象。该生成器对象是利用 
       task=[excecutor.submit(func,i) for  i in 参数化可迭代对象]
       然后将这个tasks生成器对象通过 as_completed( tasks) 函数处理，遍历整个函数，当任务执行完毕后会依次生成
       推荐使用这种，因为相比map而言，它本身返回的future实例，是不阻塞的。
       
'''

print("---------------单个函数，多个参数，"
      "借助future实例的submit方法和as_completed函数执行，"
      "先将列表中的多个任务依次进行submit,然后返回个可迭代对象，"
      "将这个可迭代对象放入as_completed函数中依次执行，他的future实例的result方法是不阻塞的")

import os
print(os.cpu_count()),

with ThreadPoolExecutor(max_workers=3) as excecutor:
      tasks=[excecutor.submit(load_url,u)for u in urs]
      for future_as in as_completed(tasks):
            print("查看是否结束:",future_as.done())
            print("查看任务执行结果:",future_as.result(),"查看回调情况：",future_as.add_done_callback(huidiao))