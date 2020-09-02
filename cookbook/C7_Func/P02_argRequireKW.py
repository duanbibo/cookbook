
'''
希望函数中的某些参数强制使用关键字参数传递 ，一个参数列表中只能用一次：
 表现方式 ：  open('c://user/...')    =>  open( file='')   必须通过这种方式
 使用方式，放在参数的前面  并且用逗号隔开
          rec(*maxsize)
          rec(maxsize,*,block,)

 目的：很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加有可读性


'''
def KW(maxsize,*,lock1):
      print(maxsize*lock1)

# k1=KW(4,1)                    这种是不可以的，IDE都校验不过去
k2=KW(4,lock1="1")
print(k2)