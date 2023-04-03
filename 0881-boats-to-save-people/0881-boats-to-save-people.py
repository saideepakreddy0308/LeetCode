class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # Given, people[i] <= limit
        
        # Greedy Approach
        # 1. Heaviest person can share a boat with the lighest person, otherwise they get their own boat
        # 2. Lighest person can pair with anyone, they might as well as with the heaviest person
        
        # Algorithm
        # if people[i] = currently lighest person; people[j] = heaviest person
        # if people[i] + people[j] <= limit, otherwise the heaviest boat sits in their own boat
        
        
        people.sort()
        
        i,j = 0,len(people)-1
        ans = 0
        
        while i<=j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans