# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # reverse second half of list
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        list2 = slow.next
        slow.next = None
        list1 = head

        list2 = self.reverseList(list2)

        while list1 and list2:
            next1, next2 = list1.next, list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
        