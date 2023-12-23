class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_l_h = []
        max_r_h = []
        total_sum = 0
        x = 0
        y = 0
        
        for i in range(len(height)):
            x = max(x, height[i])
            max_l_h.append(x)
        
        for j in range(len(height)-1,-1,-1):
            y = max(y,height[j])
            max_r_h.append(y)
        
        max_r_h = sorted(max_r_h, reverse = True)
        
        for k in range(len(height)):
            total_sum += min(max_l_h[k], max_r_h[k]) - height[k]
        
        
        return total_sum
        