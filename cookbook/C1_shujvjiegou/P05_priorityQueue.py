import heapq

'''
优先级队列  :插入的时候需要传入值和队列等级， 取出的时候按照队列等级取出
            如果两个元素优先级同样的话，默认取出先插入的元素
            https://blog.csdn.net/qq_35883464/article/details/99410423?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
  
  利用heapq模块实现 ：
  1. heapq.heappush函数把一个元组数据插入到了一个数组中 
2. heapq.heappop函数总是返回最小的元素 
3. 我们使用元组(-priority, self._index, item)的原因是：
   为了更加方便的做比较，如果有相同优先级的priority，则按插入顺序index进行比较，
   因为index永远不会重复（一定会比较出结果），所以即使后面的item为不可以比较的元素也无妨。

由于 push 和 pop 操作时间复杂度为 O(log N)，其中 N 是堆的大小，
         因此就算是 N 很大的时候它们运速度也依旧很快。


堆是非线性的树形的数据结构，有两种堆,最大堆与最小堆。（ heapq库中的堆默认是最小堆）

最大堆，树种各个父节点的值总是大于或等于任何一个子节点的值。

最小堆，树种各个父节点的值总是小于或等于任何一个子节点的值。

我们一般使用二叉堆来实现优先级队列,它的内部调整算法复杂度为logN。

堆是一个二叉树，其中最小堆每个父节点的值都小于或等于其所有子节点的值。

整个最小堆的最小元素总是位于二叉树的根节点。

'''

class PriorityQueue:
      def __init__(self):
            self._queue=[]
            self._index=()

      def push(self,item,priority):
            #核心就是这个方法
            heapq.heappush(self._queue,(-priority,self._index,item))
            self._index+=1

      def pop(self):
            #取出优先级最高的，使用切片[-1]每次从尾部取出
            return heapq.heappop(self._queue)[-1]



q=PriorityQueue()
q.push('ddd',5)
q.push('6dd',6)
q.push('3dd',3)
print(q.pop)