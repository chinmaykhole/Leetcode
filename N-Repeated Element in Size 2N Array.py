class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n=len(A)//2
        dict={}
        for i in A:
            dict[i] = dict.get(i,0)+1
        for key,value in dict.items():
            if value == n:
                return key
        
        