import logging
import  logging.config
import logging.handlers



''''
 logging 分为三个模块：
          第一个模块就是init文件也是核心文件，主要顶一下logging的单例模式，一些基础配置信息文件，句柄之类的
          第二个模块式config模块，提供了多种的配置， 在init的basicConfig的基础上支持字典类的配置，可以对文件的字典提供支持
          第三个就是handlers模块，提供了文件配置的备份、大小设置、自动清洗等功能。         

'''
def  main():

      #通过函数配置 basicConfig
      logging.basicConfig(
            #输出到文件中
            filename='app.log',
            level=logging.INFO,

      #配置日志输出样式：级别、时间、内容
      format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')


      fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # 设置日志格式
      #通过属性配置 ,这个配置控制台的输出句柄
      sc=logging.StreamHandler()
      sc.setFormatter(fmt=fmt)
      sc.setLevel('INFO')

      #这一步是关键，将设置好的logging配置，添加到handler中取，才能够生效
      logging.getLogger().addHandler(sc)

      logger=logging.getLogger()



      #需要导入 logging.conf 包

      #通过配置文件 .init文件
      #logging.config.fileConfig()


      #通过字典配置，可以写yaml文件，然后直接读字典
      #logging.config.dictConfig()



      #高级配置，需要导入logging.handles配置文件的大小，间隔时间，备份数量等
      #logging.handlers.TimedRotatingFileHandler(filename='',backupCount=4,interval=5)



      hostname='www.python.org'
      item='spam'
      filename='data.csv'
      mode='r'

      #5个级别的日志错误，以及对应的提示信息 message
      logging.critical('Host %s unknow',hostname)
      logging.error('Couldnt find %r',item)
      logging.warning('Feature is deprecated')
      logging.info('Opening file %r ,mode=%r',filename,mode)
      logging.debug('Got here')

if __name__ == '__main__':
    main()
