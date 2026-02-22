import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r=int(math.isqrt(c))   #根号后为整数
        l=0
        while l<=r:   #存在两个数相同的时候
            if (l*l)+(r*r)==c:
                return True
            elif (l*l)+(r*r)>c:
                r-=1
            else:
                l+=1
        return False
