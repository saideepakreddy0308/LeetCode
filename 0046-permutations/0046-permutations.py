class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # useing dfs to explore all systematically
        
        def dfs(path,used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    
                    dfs(path, used)
                    
                    # reverting back to current recursive call
                    used[i] = False
                    path.pop()
        
        result = []
        used = [False] * len(nums)
        dfs([],used)
        return result