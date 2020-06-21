class Solution:
    def findKthLargest(self, nums, k):
        ans=sorted(nums,reverse=True)
        return ans[k-1]
        
        