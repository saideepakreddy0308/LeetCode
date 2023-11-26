class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # Convert nums to strs for easy comparisons
        nums_str = [str(num) for num in nums]
        
        # Custom comparison function for sorting
        def compare(x, y):
            return int(x+y) - int(y+x)
        # Here, determines the order in which two numbers should be placed to form the largest number.
        
        # Sort the numbers using the custom comparison function
        nums_str.sort(key=cmp_to_key(compare),reverse = True)
        
        # Join the sorted numbers to form the largest number
        result = ''.join(nums_str)
        
        # Handle special case, when result is '0'
        return result if result[0] != '0' else '0'
    
    # t.c: O(nlogn), custom involves comparing each pair of nums, and sort operation
    # s.c: O(n),nums_str
        