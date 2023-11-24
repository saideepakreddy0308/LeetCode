class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        l = 0
        product_wo_zero = 1
        
        for i in nums:
            if i == 0:
                zero_count += 1
                l += 1
            else:
                product_wo_zero  *= i
                l += 1
         
        res = []
        
        if zero_count > 1:
            return [0] * l
        elif zero_count == 1:
            for i in nums:
                if i == 0:
                    res.append(product_wo_zero)
                else:
                    res.append(0)
        else:
            for i in nums:
                res.append(product_wo_zero // i)
        
        return res