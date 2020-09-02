




''' lambda表达式 称为匿名函数'''

'''
   语法           lambda  形参： 执行体       
       1 冒号前面的是lambda的形参，右边是执行体的结果，类似return语句
         可以是lambda对象调用传进来的参数。
        例子： l=lambda x:x*2    l(4)   ，在执行时会将4这个实参传入lambda表达式的左边
       sorted(dict,key=lambda x:x.item())  
        在一个生成器函数中，lambda的参数可以是第一个可迭代对象。
        
'''

li=[[4,1,1,1],[3,2,2,2],[2,3,3,3],[1,4,4,4]]
lis=sorted(li,key=lambda x:x[0]) #按照可迭代对象的子元素第一个索引排序
print(lis)


print("================")
x=10
a=lambda y:x+y
 #在这打印a() 是没问题的，在值的修改前调用
a1=lambda y,x=x:x+y

x=20
b=lambda y:x+y

print(a(10),b(10))
#打印30的原因
'''
在于 lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不
是定义时就绑定，这跟函数的默认值参数定义是不同的.
 如果定义一个值，然后直接运行一个函数就没问题，后面再改不影响当前函数变量的引用
 另一解决方式： 在栏目表达式中，左边声明个内部变量接受传进来的入参值，然后表达式后面的函数体引用内部变量。
 
 
'''
print(a1(10)) #这次就正确了


'''
lambda表达式在循环体中的问题
'''

func1=[lambda x:x+n for n in range(5)]
for f in func1:
      print(f(0))

func2=[lambda x,n=n:x+n for n in range(5)]
for f in func2:
      print(f(0))