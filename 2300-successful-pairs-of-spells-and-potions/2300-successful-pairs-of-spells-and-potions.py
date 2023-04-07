class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Approach - 1 : Sorting + Binary Search
        
        # Sort portions array in increasing order
        potions.sort()
        # 'answer' array to store result
        answer = []
        # length of potions array
        m = len(potions)
        # maximum potion in the potions array
        maxPotion = potions[m-1]
        
        for spell in spells:
            # minimum potion to make spell successful
            minPotion = ceil(success/spell)
            
            # Case when, if minPotion required is greater than the Max of potion array
            if minPotion > maxPotion:
                answer.append(0)
                continue
                
            # Binary Search for lower bound
            left = 0
            right = m 
            
            while left < right:
                mid = left + (right-left)//2
                
                if potions[mid] >= minPotion:
                    right = mid
                else:
                    left = mid + 1
                    
            if left < m and potions[left] >= minPotion:
                answer.append(m-left)
            else:
                answer.append(0)
            
        return answer
        