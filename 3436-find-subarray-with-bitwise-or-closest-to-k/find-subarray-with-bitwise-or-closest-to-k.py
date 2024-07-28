class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)        
        bitCount = [0] * 32 # frequency of each bit being set to 1
        
        def getRes():
            res = 0
            for i in range(32):
                if bitCount[i] > 0: 
                    res |= 1 << i
            return res
        
        def addNum(left, right, num): 
            for i in range(32):
                if (num >> i) & 1:
                    bitCount[i] += 1 
            return getRes()
        
        def removeNum(num):
            for i in range(32):
                if (num >> i) & 1: 
                    bitCount[i] -= 1 
                    
        res = float('inf')
        right = 0
            
        for left in range(n): 
            while right < n: 
                if addNum(left, right, nums[right]) < k: 
                    right += 1
                else: 
                    break


            # get diff when bit result >= k 
            if right < n: 
                res = min(res, getRes() - k)
                removeNum(nums[right]) # remove nums[right]
            
            # get diff when bit result < k
            if right > left: 
                res = min(res, k - getRes()) # excluding nums[right]
                
            removeNum(nums[left])
            # print(bitCount)
                    
        return res

# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         current_or = 0
#         res = float('inf')
#         right = 0

#         def addNum(num):
#             nonlocal current_or
#             current_or |= num

#         def removeNum(left, right):
#             nonlocal current_or
#             # Recalculate the OR for the current window
#             current_or = 0
#             for i in range(left, right + 1):
#                 current_or |= nums[i]

#         for left in range(n):
#             while right < n:
#                 addNum(nums[right])
#                 if current_or > k:
#                     right += 1
#                 else:
#                     # If the current OR <= k, we stop extending the window
#                     break
            
#             if right < n:
#                 res = min(res, abs(k - current_or))
            
#             if right > left:
#                 res = min(res, abs(current_or - k))
            
#             removeNum(left + 1, right)
#             if right == left:
#                 right += 1

#         return res