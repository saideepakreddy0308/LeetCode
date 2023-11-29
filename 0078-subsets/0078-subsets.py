class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        
        backtrack(0,[])
        return result
    
    # T.C: O(2 ^ n), as each elt in nums had two choices, include it in subset or exlcude
    # S.C: O(N), depth of recursive call and space used by path, in worst case, its len of path 'n.'