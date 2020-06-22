class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = [0]*(amount+1)
        ans[0]=1
        for i in coins:
            for j in range(amount+1):
                if j>= i:
                    ans[j]+=ans[j-i]
        return ans[-1]
        
        