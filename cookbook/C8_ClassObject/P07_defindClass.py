
import bisect
class SortItems():

      def __init__(self,initial=None):
            self._item=sorted(initial)

      def __getitem__(self, item):
            return self._item[item]

      def __len__(self):
            return len(self._item)

      def add(self,item):
            bisect.insort(self._item,item)


item=SortItems([34,3423,2])
print(item.__len__())

item.add(89)
print(list(item))