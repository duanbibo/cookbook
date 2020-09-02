


'''
实现一个状态机在不同状态下执行的操作对象，不在代码中出现太多判断语句
'''

class Connection:

      def __init__(self):
            self.satus='ClOSED'
      def read(self):
            if self.satus!='OPEN':
                  raise RuntimeError('NOT OPEN')
            print('Reading')

      def write(self,data):
            if self.satus!='OPEN':
                  raise RuntimeError('Not open')
            print('writing')

      def open(self):
            if self.satus=='OPEN':
                  raise  RuntimeError('Already open')
            self.satus='OPEN'

      def  close(self):
            if self.satus=='ClOSED':
                  raise RuntimeError('Already closed')
            self.satus='CLOSED'

'''
这样写的缺点：代码复杂，好多条件判断，执行效率低，每次的操作都需要检查
  
  可以将不同的状态单独抽取一个类，利用抽象的原则。父类在构造方法写调用的
'''