

'''

接受可变长参数，在内部处理时，就不需要加星号了
'''
def func(first,*args):
      if args==None:
            return  first
      else:
            return (first + sum(args)) / (1 + len(args))


a=func(5)
b=func(5,4,5)
print(a,b)

'''
试着创建一个HTML文档  :其中class的值是一个列表，css的值是一个字典
<input calss=" passwd,input "   css=" XX=5px ;groupclore=blue" playhold="">
     请输入密码
</input>
'''

def make_html(tag,value,*arg,**attrs):
      keyvale=['%s=%s'%(k,v)for k,v in attrs.items()]
      attr=''.join(keyvale)
      print(attr)
      html= '<{tag} class={arg} {attr}>{value}</{tag}>'.format(tag=tag,arg=arg,value=value,attr=attr)
      return  html
html=make_html("input","请输入账号","passwd",passwd="passwd")
print(html)

'''
练习： 遍历kwargs
'''

