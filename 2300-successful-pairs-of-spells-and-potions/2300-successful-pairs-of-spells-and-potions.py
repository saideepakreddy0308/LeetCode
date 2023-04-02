class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        # Sort the potions array in increasing order
        potions.sort()  # O(mlogm)
        
        # to store the result
        answer = []
        
        #m, length of potions array
        m = len(potions)
        
        #max value in the potions array
        maxPotion = potions[m-1]
        
        for spell in spells:  #O(n*logm)
            # minPotion to make spell successful = ceil(success/spell), what the index 
            minPotion = (success + spell - 1)// spell
            # minPotion = ceil(success/spell)
            
            # Case when, if minportion > maxportion, means it will not be possible
            if minPotion > maxPotion:
                answer.append(0)
                continue
            # But if its inside the maxPotion, find index, finding lower bound
            index = bisect.bisect_left(potions,minPotion)
            #append answer
            answer.append(m-index)
        
        return answer
    
    # Time Complexity: O(mlogm + nlogm) = O((m+n)*logm)
    # Space Complexity: O(m); sort() method sorts a list using the Timsort Algorithm, where m is the number of the elements.