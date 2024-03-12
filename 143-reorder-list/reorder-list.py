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
            return

        # get head of second half of the linked list
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # if the linked list has even number of nodes then slow will be pointing to start of second half (fast is null)
        # otherwise, slow will be pointing to node before second half (fast is not null), so we move it forward one step
        if fast:
            prev = slow
            slow = slow.next

        # disconnect the two halves
        prev.next = None

        secondHalf = slow

        # reverse second half of the list
        secondHalf = self.reverseList(secondHalf)

        # reorder both halves
        firstHalf = head

        while firstHalf and secondHalf:
            firstHalfNext = firstHalf.next
            secondHalfNext = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = firstHalfNext

            firstHalf = firstHalfNext
            secondHalf = secondHalfNext
        