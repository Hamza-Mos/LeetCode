# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow will point to last node in first half of list
        head2 = slow.next
        slow.next = None

        head2 = self.reverseList(head2)

        head1 = head

        while head1 and head2:
            head1Next, head2Next = head1.next, head2.next

            head1.next = head2
            head2.next = head1Next

            head1 = head1Next
            head2 = head2Next
            
        