class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        nums.sort()
        midIndex =  len(nums) // 2   # finding median
        
        # Helper functions
        
        def check_palindrome(x):
            x = str(x)
            return x == x[::-1]
        
        # total cost function
        def total_cost(nums, target):
            result = 0
            for elem in nums:
                result += abs(elem - target)
            return result
        
        # finding median
        if len(nums) % 2 == 1:
            mid = nums[midIndex]
            if check_palindrome(mid):
                return total_cost(nums,mid)
        
        else:     # even number of nums
            mid = (nums[midIndex] + nums[midIndex - 1]) // 2
            if check_palindrome(mid):
                return total_cost(nums,mid)
        
        # None of it is palindrome, so notsuceeded after these attempts,then
        
        p_1 = mid + 1
        p_2 = mid - 1
        
        # we try to find palindrome, one less than , and other greater than median element
        while not (check_palindrome(p_1) and check_palindrome(p_2)):  # if both palindromic, true, exit to checkout the min total_cost.
            # (10,[11],12); (20,21,[22]); ([33],34,35)
            if not check_palindrome(p_1):
                p_1 += 1
            if not check_palindrome(p_2):
                p_2 -= 1
            
        return min(total_cost(nums,p_1), total_cost(nums,p_2))
           