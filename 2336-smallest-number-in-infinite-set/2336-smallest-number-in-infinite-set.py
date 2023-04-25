from sortedcontainers import SortedSet

class SmallestInfiniteSet:


    def __init__(self):
        self.added = SortedSet()
        self.curr = 1

    def popSmallest(self) -> int:
        if len(self.added):
            ans = self.added[0]
            self.added.discard(ans)
        else:
            ans = self.curr
            self.curr+=1
        return ans

    def addBack(self, num: int) -> None:
        if self.curr<=num or num in self.added:
            return
        self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
