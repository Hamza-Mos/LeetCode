# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            curr.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

            curr = curr.next

        return dummy.next
        