# In this way, the higher the weight, the larger the cumulative probability, making it more likely to be chosen randomly, which is in line with the given probability distribution.

import random
import bisect

class Solution:

    def __init__(self, weights):
        total_weight = sum(weights)
        self.cumulative_probs = [0]

        # Calculate cumulative probabilities
        for weight in weights:
            probability = weight / total_weight
            self.cumulative_probs.append(probability + self.cumulative_probs[-1])

    def pickIndex(self):
        # Generate a random number between 0 and 1
        random_number = random.random()

        # Find the position where the random number would fit in the cumulative probabilities
        index = bisect.bisect_right(self.cumulative_probs, random_number) - 1

        return index
