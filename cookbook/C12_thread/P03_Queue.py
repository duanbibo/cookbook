from queue import Queue
from threading import Thread
from time import  sleep

'''
多线程通信 ：线程之间安全的交换信息或数据，
Queue对象已经包含了必要的锁，所以你可以在多线程间多安全的共享数据。当使用队列式，
调用生产者和消费者的关闭问题，需要在队列中放着一个值，当消费者读到这个值的时候，终止执行

python queue模块有三种队列:
针对这三种队列分别有三个构造函数:
1、class Queue.Queue(maxsize) FIFO ，设置队列大小，值为非正数无限循环队列
2、class Queue.LifoQueue(maxsize) LIFO 
3、class Queue.PriorityQueue(maxsize) 优先级队列 
介绍一下此包中的常用方法:

Queue.qsize() 返回队列的大小 
Queue.empty() 如果队列为空，返回True,反之False 
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应 
Queue.get([block[, timeout]])从陪你过队列中删除元素并返回该元素的值
Queue.get_nowait() 相当Queue.get(False)
非阻塞 Queue.put(item，block,timeout) 写入队列，默认非阻塞block=False ,timeout等待时间 
当队列满的时候，
 如果block设置为True，timeout为None为阻塞队列,timeout设置后在时间内执行或者抛出Full异常
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作，阻塞直至队列为空



设置队列大小的意义：对于生产者与消费者速度差异，可以控制队列的缩小来进行阻塞。

'''

q=Queue(maxsize=0)

def product(name):
      '''每秒生产10个元素'''
      num=1
      while True:
            num += 1
            q.put('生产者{}'.format(num))
            print('{}训练{}只'.format(name, num))

            print("生产者现有多少个元素", q.qsize())
            sleep(0.1)


def consume(name):
      '''每秒消耗2.5个元素'''
      while True:
            print('{}消耗了{}'.format(name,q.get()))
            sleep(0.4)
            print("消耗者{}查看现有多少个元素".format(name),q.qsize())
            #print( q.task_done())


t1=Thread(target=product,args=('p1',))
t2=Thread(target=consume,args=('c1',))
t3=Thread(target=consume,args=('c2',))
# t1.start()
# t2.start()
# t3.start()

'''
如果一个线程需要在一个消费者线程处理完数据项时立即得到通知，可以把要发送的数据和一个Event放到一起使用。
这样生产者就可以通过这个Event对象来检测处理过程

'''
import  urllib3
from urllib import request
import os

class DownloadThread(Thread):
      def __init__(self,queue):
            Thread.__init__(self)
            self.queue=queue

      def run(self):
            while True:
                  #从队列中取出一个url元素
                  url=self.queue.get()
                  print(self.name+"begin download"+url+"...")
                  self.download_file(url)
                  self.queue.task_done()

                  print(self.name+"download completed!!!")

      def download_file(self,url):
            #利用URLopen函数获取网页数据，获取的数据是二进制数据如果需要解析，需要二进制数据解码。
            urlhandler=request.urlopen(url)
            print(urlhandler)
            fname=os.path.basename(url)+".html"
            print(fname,"fname")
            with open(fname,'wb')as f:
                  while True:
                        chunk=urlhandler.read(1024)
                        if not chunk:
                              break
                        f.write(chunk)

if __name__ == '__main__':

            urls = ["http://ww.baidu.com", "http://360.com"]
            queue = Queue()
            for i in range(5):
                  t = DownloadThread(queue)
                  t.setDaemon(True) #将现场设置后台，与下面的队列的join方法一块使用，首先阻塞守护进程，执行所有对列中的元素然后不阻塞后台进程。
                  t.start()
            for url in urls:
                  queue.put(url)
            queue.join() #等待队列元素为空时，才不阻塞



