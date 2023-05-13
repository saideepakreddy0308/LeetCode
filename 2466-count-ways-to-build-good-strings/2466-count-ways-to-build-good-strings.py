class Solution:
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    MAX = 1000000007
    table = [0]*(high+1)
    table[zero] += 1
    table[one] += 1
    start = min(zero, one)

    for i in range(start, high+1):
      # Fill in table[i]
      if i-zero >= 0:
        table[i] += table[i-zero] % MAX
      if i-one >= 0:
        table[i] += table[i-one] % MAX
    
    total_count = 0
    for i in range(low, high+1):
      total_count += table[i] % MAX
    return total_count % MAX