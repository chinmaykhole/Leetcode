class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = [amount+1] * (amount+1)
        ans[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    ans[i] = min(ans[i], ans[i-c] + 1)

        if ans[amount] == amount+1:
            return -1
        return ans[amount]