class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     output = int(a,2) + int(b,2)
    #     return "{:b}".format(output)
# T.C: O(N) for casting to int + O(log(output)) back to binary

    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry > 0:
            x = int(a[i]) if i >= 0 and a[i] == '1' else 0
            y = int(b[j]) if j >= 0 and b[j] == '1' else 0

            total = x + y + carry
            ans.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(ans[::-1])
    
    # Both t.c and s.c are O(max(len(a), len(b))
        