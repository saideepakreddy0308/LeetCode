class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            count = 0
            b_num = str("{:b}".format(i))
            for i in b_num:
                if int(i) == 1:
                    count +=1
            l.append(count)
        return l