class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans = [0,0]
        for i in moves:
            if i == 'U':
                ans[0] -= 1
            elif i == 'D':
                ans[0] += 1
            elif i == 'L':
                ans[1]-=1
            else: ans[1]+=1
        return ans == [0,0]