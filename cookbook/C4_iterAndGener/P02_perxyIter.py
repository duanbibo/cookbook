'''
委托迭代二：
通过属性进行迭代，在iter魔法函数内，调用iter()方法，方法的参数指向实例的序列属性
'''

class Node:

      def __init__(self,value):
            self.value=value
            self.children=[]

      def  add_children(self,node):
            self.children.append(node)

      def  __iter__(self):

            return iter(self.children)




if __name__ == '__main__':
    from collections import Iterator, Iterable
    n=Node(0)
    print(isinstance(n,Iterator))  #不是迭代器
    n.add_children(4)
    n.add_children(3)
    n.add_children(5)
    for i in n:
          print(i)


