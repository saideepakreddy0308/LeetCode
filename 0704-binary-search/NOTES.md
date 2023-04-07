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
Approach - 5
```
import bisect
​
class Solution:
def search(self, nums: List[int], target: int) -> int:
# Find the insertion position `idx`.
# This method uses lower_bound or bisect.bisect_left
idx = bisect.bisect_left(nums, target)
​
if idx < len(nums) and nums[idx] == target:
return idx
else:
return -1
# T.C : O(logN)
# S.C : O(1)
​
```
​