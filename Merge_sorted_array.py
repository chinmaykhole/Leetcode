class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not(nums1 or not nums2):
            return False
        nums1[m:m+n]=nums2[:n]
        return nums1.sort()        
            