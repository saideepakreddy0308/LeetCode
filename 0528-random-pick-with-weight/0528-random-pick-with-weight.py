import random
class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.total_weight = sum(w)

    def pickIndex(self) -> int:
        target = random.uniform(0,self.total_weight)
        current_sum = 0
        
        # Iterate throught the weights and find the index where the random number falls
        for i, weight in enumerate(self.weights):
            current_sum += weight
            if target < current_sum:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()