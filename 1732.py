class Solution:
    def largestAltitude(self, gain):
        diff=0
        n=len(gain)
        prefix=[]
        for i in range(n):
            diff=gain[i]+diff
            prefix.append(diff)

        return max(prefix) if max(prefix)>0 else 0

s=Solution()
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))

"""
优化版本，不需要额外的数组，用一个单独的变量记录,空间复杂度从O(n)->O(1)
"""
def largestAltitude(self, gain):
    altitude = 0
    max_alt = 0

    for g in gain:
        altitude += g  # 当前海拔（前缀和）
        max_alt = max(max_alt, altitude)

    return max_alt