class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return False
        
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num,num+cur_sum)
            max_sum = max(cur_sum,max_sum)
            
        return max_sum
        