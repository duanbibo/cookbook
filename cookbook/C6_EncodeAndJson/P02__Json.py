import  json


''''
 dump：编码  =》转化为字符串的过程
 load :解码   =》转化为python字典的过程
  

'''
data={ "1":'1value','2':'2value'}
print(type(data))

''' dumps :将字典转化为字符串'''
json_str=json.dumps(data)
print(json_str,type(json_str))


'''  dump可以将字典的类型数据直接dump解析到文件中'''
# with open('json.json','w')as f:
#       json.dump(data,f)



''' 使用loads方法将str转换为dict'''
with open(r'json.json','r')as f:
      file_str= f.read()
      json_str2=json.loads(file_str)
      print(json_str2,type(json_str2))





with open(r'json,json','r')as f:
      jl=json.load(f)
      print(jl)