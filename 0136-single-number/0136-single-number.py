class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            print(s,i,s^i)
            s^=i
            print(s)
        return s