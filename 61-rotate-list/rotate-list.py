# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self, firstPtr, lastPtr):
        lastPtr.next = firstPtr

        curr = lastPtr

        while curr.next != lastPtr:
            curr = curr.next

        curr.next = None

        return [lastPtr, curr]

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # get length
        length = 1
        curr = head

        while curr.next:
            curr = curr.next
            length += 1

        lastPtr = curr
        firstPtr = head

        k = k % length

        while k:
            firstPtr, lastPtr = self.rotate(firstPtr, lastPtr)
            k -= 1

        return firstPtr