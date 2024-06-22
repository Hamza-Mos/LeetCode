# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numList = []

        curr = head

        while curr:
            numList.append(curr.val)
            curr = curr.next

        left, right = 0, len(numList) - 1

        while left < right:
            if numList[left] != numList[right]:
                return False

            left += 1
            right -= 1

        return True
        