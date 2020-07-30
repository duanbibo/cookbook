

'''
题目：去除列表中重复的数据并且保持顺序不变
   直接用set是不行的 ,自己编写set的内部实现也不行的，
    必须使用生成器函数，依次根据可迭代对象的yield顺序生成，因为调用add后出来的会根据大小升序，
    获取生成器函数对象后，再调用list方法或for循环遍历，依次数据，

'''
li=[1,4,3,5,2,4,7,1]  #[1,4,3,5,2,7]


def doset(list):
      se=set()
      for i in list:
            if i not in se:
                  yield  i
                  se.add(i)

#

print(list(doset(li)))


def dedupe2(items, key=None):
    """元素不是hashable的时候 ，并且支持根据传入的自定义key的值进行排序"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
