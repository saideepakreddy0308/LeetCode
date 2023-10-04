class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        if n == 0:
            return 0
        
        index = 1
        elt = arr[0]
        
        for i in range(1,n):
            if arr[i] != elt:
                # Found a new unique element
                arr[index] = arr[i]
                index += 1
                
                #update elt to new unique elt
                elt = arr[i]
        
        return index 