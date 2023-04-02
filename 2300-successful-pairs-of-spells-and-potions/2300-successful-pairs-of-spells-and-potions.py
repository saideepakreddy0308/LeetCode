class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sorting + Two Pointers Approach
        # 1. if spell = a ; minPotion = b, then spell * minPotion = success; For spell > a , then minimum required potion will be all minPotion <= b, if we need result >= success
        # 2. If both spell and potions array are sorted in increasing order; two pointers - one to smallest spell; other to largest potion
        # 3. If product of current spell and potion >= success, then we keep decreasing the second pointer to point to a smaller potion.
        # 4. We stop if we dont form a successful pair, we count all previous approach.
        
        sortedSpells = [(spell,index) for index,spell in enumerate(spells)]
        
        # Sort the ' spells with index' and 'potions' array in increasing order
        sortedSpells.sort()  # O(n*logn)
        print(sortedSpells)
        potions.sort() # O(m * logm)
        
        answer = [0] * len(spells)
        m = len(potions)
        potionIndex = m - 1
        
        # For each 'spell' find the respective 'minPotion' index
        for spell, index in sortedSpells:   # O(n + m); we use two pointers and iterate on each element of the sortedSpells and potions array 
            while potionIndex >= 0 and (spell * potions[potionIndex]) >= success:
                # potionIndex is updated and doesn't change for each spell
                potionIndex -= 1
            answer[index] = m - (potionIndex + 1)
        return answer
    
    # Time Complexity: O(n*logn) + O(m*logm) 
    # Space Complexity: O(n + m), in python we use extra space to sort arrays in place
            