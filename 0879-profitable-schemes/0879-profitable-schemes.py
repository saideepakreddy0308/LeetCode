class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def helper(i, member, prof):
            if i==len(group):
                return 1 if prof>=minProfit else 0
            ans = 0
            if member+group[i]<=n:
                    ans = helper(i+1, member+group[i], min(prof+profit[i],minProfit))
            return (ans+helper(i+1, member, prof))%(10**9 + 7)
        return helper(0,0,0)
