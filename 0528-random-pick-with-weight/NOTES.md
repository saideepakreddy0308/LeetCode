T**Topic 1:**
The addition of the previous cumulative probability in the line self.cumulative_probs[i] += self.cumulative_probs[i - 1] is to ensure that each element in self.cumulative_probs represents the cumulative probability up to that index.
​
Let's break it down with an example:
​
Suppose you have weights [2, 3, 1], and you want to calculate the cumulative probabilities.
​
Initially, cumulative_probs is [2/6, 3/6, 1/6] which is [1/3, 1/2, 1].
After the loop, cumulative_probs becomes [1/3, 5/6, 1].
​
Now, if you want to find the cumulative probability at index 2, you do:
​
cumulative_probs[2] = cumulative_probs[1] + probability of weight at index 2
​
This ensures that cumulative_probs[2] represents the cumulative probability up to that point.
**Topic 2**
Random Number:
If random_number = 0.2, it falls into the first interval [0, 1/6) and corresponds to the first weight (index 0).
If random_number = 0.5, it falls into the second interval [1/6, 3/6) and corresponds to the second weight (index 1).
If random_number = 0.8, it falls into the third interval [3/6, 6/6) and corresponds to the third weight (index 2).
​
This way, using cumulative probabilities, we map a random number to an index based on the probabilities assigned to each element. The larger the weight, the larger the interval, and thus, the higher chance it will be selected.
​
**Topic 3**
bisect.bisect_right(self.cumulative_probs, random_number) finds the position where random_number would fit in the cumulative distribution.
Subtracting 1 gives us the index in the cumulative_probs list, which corresponds to the index in the original list.
**Topic 4**
random.random():
​
This function generates a random float between 0 and 1. It's used to simulate the random selection proces