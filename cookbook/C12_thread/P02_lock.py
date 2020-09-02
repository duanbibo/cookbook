import threading
from threading import Thread


'''
同步原句： l= threading.Lock   
l.acquire()   加锁
l.release()   释放锁
推荐使用with语句，或者try .. finally

  其他同步原句： Rlock,event，condition，信号量
   
'''

l=threading.Lock()  #使用threading模块的lock类

g=0
def forrange(x):
      for i in range(x):
            with l:                                  #这里如果没有锁的话，多个线程进行累加造成计算的结果会小于实际结果
                  global g
                  g+=i
                  #print(i)

def  fortry(x):
      '''使用
       try:
                lock.acquire
       fially:
                  lock.release() '''
      for i in range(x):
            try:
                  l.acquire()
                  global g
                  g+=i
            finally:
                  l.release()



t1=threading.Thread(target=forrange,args=(100000,))
t2=threading.Thread(target=fortry,args=(100000,))
t3=threading.Thread(target=forrange,args=(100000,))

t1.start()
t2.start()
t3.start()

t1.join()#当子线程执行较为耗时时，对于main线程的守护进程执行完毕后就停止了，无法继续执行其他线程的内容，
 # 通过调用当前线程.join()方法，让主线程阻塞，等待当前调用的线程执行完毕后在调用main线程的内容
t2.join()
t3.join()

print(g)

'''
Semaphore 信号量
                          sema=threading.Semaphore(5)初始化信号量的数量
                          sema.acquire()  每次执行前面进行加锁，
                          sema.release()    执行后进行释放信号量
                          
'''
def  work (n,sema):

      print('Working',n)

sema=threading.Semaphore(5)
sema.release()
nworkers=10
for n in range(nworkers):
      t=threading.Thread(target=work,args=(n,sema))
      t.start()


'''
同步原句 event：

          event=threading.Event()          #事件类 创建一个事件管理标志，该标志（event）默认为False
         event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
             event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒；
            event.clear()：将event的标志设置为False，调用wait方法的所有线程将被阻塞；
            event.isSet():返回布尔值类型，event的标志。
            
      用法： 可以将event注册到子线程内，子线程在内部使用event.wait()方法进行阻塞，
            主线程通过event.set重新唤醒子线程 ，
            主线程通过event.clear 方法 将唤醒的线程阻塞

'''
event=threading.Event()          #事件类
from time import  sleep

def eventtest(n, event):

    while not event.isSet(): #2.初始化管理标志位false  ，进行混循环
         print ('Thread %s is ready' % n)
         sleep(1)

    event.wait()    #   3.当前线程阻塞

    while event.isSet():   #5.主线程调用set方法，将状态设置为true，重新激活子线程并通知。开始循环打印
         print ('Thread %s is running' % n)
         sleep(1)

def main():
      event = threading.Event()
      for i in range(0, 2):
            th = threading.Thread(target=eventtest, args=(i, event))
            th.start()   #1.第一步进入线程内部执行,
      print("sleep before")  # 1.1同时主线程也在交替执行
      sleep(3)               #1.3主线程休眠
      print( '----- event is set -----') #3.1子线程阻塞后，只打印主线程的内容

      event.set() #4.在主线程内调用set,将标志设置为true
      sleep(3)          #4.主线程内部休眠，不影响子线程
      print('----- event is clear -----')
      event.clear()  #6.在主线程内调用方法，设置调用wait方法进行阻塞，设置状态为false，控制子线程变为阻塞，定制循环

main()

'''
Condition :条件
   
    基于锁的加锁和释放acquire ,和release方法，在内部进行调用 wait和notify方法进行通知其他线程。
     加锁和释放锁与wait和通知之间的关系。 锁需要包括wait或notify方法，在通知时仍没有释放锁。 
      
     with con:
          con.wait()
      
     with con:
          con.notify()
          


'''
class Account:
      def __init__(self,balance=0):
            self.balaence=balance

            lock=threading.Lock()
            self.con=threading.Condition(lock)

      def getMoney(self,money):
            with self.con:
                  while money > self.balaence:
                        self.con.wait()#取钱金额大于现有金额阻塞
                  new_blaence=self.balaence-money
                  self.balaence=new_blaence

      def postMoney(self,money):
            with self.con:
                  self.balaence+=money
                  sleep(0.1)
                  self.con.notifyAll()

import random
from  concurrent.futures import ThreadPoolExecutor
def add_money(account):
      while True:
            money=random.randint(5,10)
            account.postMoney(money)
            print(threading.current_thread().name,":",money,'====>',account.balaence)
            sleep(0.5)

def sub_money(account):
      while True:
            money=random.randint(10,30)
            account.getMoney(money)
            print(threading.current_thread().name,":",money,'====>',account.balaence)
            sleep(1)

def mainCon():
      account=Account()
      with ThreadPoolExecutor(max_workers=10) as pool:
            for i in range(5):
                  pool.submit(add_money,account)
                  pool.submit(sub_money,account)

mainCon()