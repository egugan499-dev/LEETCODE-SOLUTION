class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        prefix = 1
        suffix = 1
        
        for i in range(n):
            answer[i] *= prefix
            answer[n - 1 - i] *= suffix
            
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
        
        return answer