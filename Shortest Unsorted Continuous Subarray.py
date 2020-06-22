class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums=sorted(nums)
        start=end=0
        for i in range(len(nums)):
            if nums[i]!=snums[i]:
                start = i
                break
                
        for i in range(len(nums)-1,0,-1):
            if nums[i]!=snums[i]:
                end=i
                break
        
        return end -start+1 if end-start else 0
                
            
        