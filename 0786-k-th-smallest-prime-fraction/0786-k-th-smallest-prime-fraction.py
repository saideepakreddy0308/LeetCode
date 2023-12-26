class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        xyz = []
        
        for i in range(len(arr)-1):
            for j in range(1,len(arr)):
                xyz.append([arr[i],arr[j],arr[i]/arr[j]])
                
        xyz.sort(key=lambda x: x[-1])
        
        return [ xyz[k-1][0],  xyz[k-1][1] ]