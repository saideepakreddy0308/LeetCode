# Approach 1:
# Time: O(n+k) - Simple Approach 
# class Solution:
# 	def findKthPositive(self, arr: List[int], k: int) -> int:
# 		arr = set(arr)
# 		for i in range(1, len(arr)+k+1):  # O(n+k)
# 			if i not in arr:
# 				k -= 1
# 			if k == 0:
# 				return i

# Approach 2:
# Time: O(logn) - Binary Search Approach
class Solution:
	def findKthPositive(self, arr: List[int], k: int) -> int:
		strt = 0
		end = len(arr)-1
		while strt <= end:
			mid = strt+(end-strt)//2
			if arr[mid]-mid-1 < k:
				strt = mid+1
			else:
				end = mid-1
		return strt+k

    # For example, if arr[mid] is 7 and mid is 3, then arr[mid] - mid - 1 would be 7 - 3 - 1 = 3, which means that there are 3 missing positive integers between arr[0] and arr[mid].
        
    # The while loop in the code checks if the number of missing positive integers before arr[mid] is less than k. If this is true, it means that the k-th missing positive integer must be located to the right of the middle index mid. Therefore, the strt pointer is updated to mid + 1 to search the right sub-array. If the number of missing positive integers before arr[mid] is greater than or equal to k, then the k-th missing positive integer must be located to the left of the middle index mid. Therefore, the end pointer is updated to mid - 1 to search the left sub-array.