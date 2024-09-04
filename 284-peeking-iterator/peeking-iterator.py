# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

'''
["PeekingIterator","hasNext","peek","peek","next","next","peek","peek","next","hasNext","peek","hasNext","next","hasNext"]

[[[1,2,3,4]],[],[],[],[],[],[],[],[],[],[],[],[],[]]
         i
[null,true,1,1,1,2,3,3,3,true,4,true,4,true]
'''

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_list = deque()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.iterator.hasNext():
            self.next_list.append(self.iterator.next())
        return self.next_list[0]
        

    def next(self):
        """
        :rtype: int
        """
        if self.next_list:
            return self.next_list.popleft()

        else:
            return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        print(self.next_list)
        return len(self.next_list) > 0 or self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].