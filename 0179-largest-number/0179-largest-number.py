from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x,y):
            return int(x+y) - int(y+x)
        
        sorted_nums = sorted(map(str,nums),key = cmp_to_key(compare), reverse = True)
        
        result = ''.join(sorted_nums)
        
        return result if result[0] != '0' else '0'
        
#         nums_str = [str(num) for num in nums]
        
#         # Custom sorting key: Compare concatenated strings in descending order
#         nums_str.sort(key = lambda x: x*10, reverse = True)

"""           
class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert the list of numbers to list of strings
        nums = [str(num) for num in nums]
        
        # Sort the list of strings using our custom sorting function
        nums.sort(key=LargerNumKey)
        
        # Join the sorted list of strings to form the final result
        largest_num = ''.join(nums)
        
        # If the largest number is 0, return "0"
        # Otherwise, return the largest number
        return "0" if largest_num[0] == "0" else largest_num """ 