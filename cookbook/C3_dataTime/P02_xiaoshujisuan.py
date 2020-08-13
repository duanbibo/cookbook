from decimal import Decimal


'''
对于小数的计算，由于浮点数，无法精确表达出所有的十进制小数位，所以在计算时容易产生误差
'''
a=2.1
b=3.2
c=a+b
print(c,"两个小数相加可能数位不精确")

lixiaoshu=[1,2,-4.432,7.8,1.23]
print(sum(lixiaoshu),"计算有问题呀，又出现小数位数问题")


#传入Decimal时，必须为字符类型的数值
ad=Decimal('2.111')
bd=Decimal('53.7')
cd=ad+bd
print(ad+bd,cd)






'''  浮点型运算时，通过调用小数模块计算，会完全精确的运算，
         比如计算的和与差按照最长的小数位数，计算的乘法和除法可能造成位数更多，造成了不便
 当我们需要四舍五入时需要用到localcontext,在当前上下文中自定义精确的小数位数
  使用上下文对象句柄的.prec 可以设置当前上下文小数值精度precision，精度指的是非0的位数
        .prec =N ,设置小数点前和小数点后共同的非零位数，如果超出这个长度用科学计数法表示  11E 4 
        .prec+=N ,设置小数点后面的长度
        

         
        
 '''



from decimal import localcontext

with localcontext() as ctx:
      ctx.prec=4
      print(ad+bd)



'''ascii码排序： 先进行数字,再进行大写字母，再进行小写字母。
           数字和字母占ASCII码的48-122之前的空间'''
print(ord('0'),ord('A'),ord('z'))
print(chr(48))

