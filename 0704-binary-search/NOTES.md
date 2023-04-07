# Time Complexity: O(logn)
# Space Complexity: O(1)
```
When the value at "mid" is greater than the target, we know that the target value must be present in the left half of the array because the array is sorted in ascending order.
​
In the upper bound approach to binary search, we are looking for the position where the target could be inserted into the array without disrupting its sorted order. Since the mid element is greater than the target, we know that the target should be inserted before the mid element. Therefore, we discard the right half of the array and continue searching in the left half.
​
To summarize, taking the right pointer as mid when the mid element is greater than the target allows us to narrow down our search to the left half of the array where the target should be located based on the sorted order of the array.
​
Approach 3
```
class Solution:
def search(self, nums: List[int], target: int) -> int:
​
# Looking for target in the array, we look into insert position where we can put target, in without disrupting order
# Concept:  Find Lower Bound, here we look for leftmost insert position
left = 0
right = len(nums)
while left < right:
mid = (left + right) // 2
if nums[mid] >= target:
right = mid
else:
left = mid + 1
if left < len(nums) and nums[left] == target:
return left
else:
return -1
# Time Complexity: O(logn)
# Space Complexity: O(1)
```
Approach - 4
```
class Solution:
def search(self, nums: List[int], target: int) -> int:
# Find the insertion position `idx`.
# This method uses upper_bound or bisect.bisect_right
idx = bisect.bisect_right(nums, target)
​
if idx > 0 and nums[idx - 1] == target:
return idx - 1
else:
return -1
```
​