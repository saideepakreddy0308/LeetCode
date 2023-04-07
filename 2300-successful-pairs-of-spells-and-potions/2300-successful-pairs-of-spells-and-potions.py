class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Approach - 2 : Soring + Two pointers
        
        answer = [0] * len(spells)
        
        Sortedspells = [(spell,index) for index,spell in enumerate(spells)] 
        
        # Sort array in increasing order
        Sortedspells.sort()   # [(1,1) , (3,2), (5,0)]
        
        m = len(potions)
        potions.sort()
        potionIndex = m - 1
        
        for spell,index in Sortedspells:
            
            while potionIndex >= 0 and (spell * potions[potionIndex] >= success):
                potionIndex -= 1
            answer[index] = m - (potionIndex + 1)
        
        return answer