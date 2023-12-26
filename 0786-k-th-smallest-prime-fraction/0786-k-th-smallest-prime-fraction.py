class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lo, hi = 0, 1

        while True:
            mid = (lo + hi) / 2
            j = 0
            count = 0
            maxFrac = [0, 1]

            for i in range(len(arr)):
                while j < len(arr) and arr[i] > mid * arr[j]:
                    print(" mid is",mid," j is ", j," ", arr[i], arr[j], mid * arr[j] )

                    j += 1
                    print(" j is incremented", j)

                count += len(arr) - j
                print("count is", count)

                if j < len(arr) and maxFrac[0] * arr[j] < arr[i] * maxFrac[1]:
                    maxFrac = [arr[i], arr[j]]
                    print("maxFrac is", maxFrac, maxFrac[0] * arr[j], arr[i] * maxFrac[1] )
                    
            if count == k:
                return maxFrac
            elif count > k:
                hi = mid
            else:
                lo = mid
