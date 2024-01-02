class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        kl = {}
        has = [[]]
        k = 1
        for i in nums:
            if i not in kl:
                kl[i] = 1
            else:
                kl[i] += 1
                if kl[i] > k:
                    has.append([])
                    k += 1

            has[kl[i] - 1].append(i)
        return has