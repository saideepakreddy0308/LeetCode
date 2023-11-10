class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Floyds Algorithm -> Tortoise and Hare
         # In the Floyd's Tortoise and Hare algorithm, the movement of tortoise and hare is not a simple increment by 1 or 2. Instead, it involves accessing the next element in the array based on the current position of the pointers.
            
        
        # Phase 1: Detect if there is a cycle
        tortoise = hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            
            if tortoise == hare:
                break
        
        # Phase 2: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
