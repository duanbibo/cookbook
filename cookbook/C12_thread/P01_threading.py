import threading
import _thread

'''
python标准库中，关于多线程的库有：threading ，_thread
             threding更能使用，因为对于线程的控制更全面，生命周期更清晰。 
               如创建线程时，通过run方法进行创建线程，调用start方法进行启动线程。 _thread是直接new出来的线程，直接启动。不利于管理
               在执行线程任务时，在大背景的main线程，通过join可以控制插入线程的,threading中的join()方法能够阻塞当前上下文环境的线程，
               直到调用此方法的线程终止或到达指定的timeout（可选参数）
               _thread类创建的线程，有可能在子线程没有执行完毕后，后台线程就已经终止了。
                _thread模块不支持守护线程，thread模块中主线程退出的时候，所有的子线程不论是否还在工作，
                都会被强制结束，并且没有任何警告也没有任何退出前的清理工作
'''


def dofor(x):
      for i in range(x):
            print("线程执行体",i)


t=threading.Thread(target=dofor,args=(5,),name='dofor')
#启动线程
t.start()
#判断线程是否存活
print(t.isAlive())

class Dofor(threading.Thread):

      def __init__(self,n):
            super().__init__()
            self.n=n


      def run(self):
            for i in range(self.n):
                  print("通过类继承Thread实现内部循环",i)


d=Dofor(5)
d.start()

