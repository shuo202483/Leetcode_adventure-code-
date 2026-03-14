#二分查找+贪心
class Solution(object):
    def minDays(self, bloomDay, m, k):
        # 不可能完成的情况
        if m * k > len(bloomDay):
            return -1

        # 二分查找的范围：最小天数 ~ 最大天数
        left, right = min(bloomDay), max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            # 检查第 mid 天能否做出 m 束花
            if self.canMake(bloomDay, m, k, mid):
                ans = mid  # 可以，尝试更早的天数
                right = mid - 1
            else:
                left = mid + 1  # 不可以，需要更多天数

        return ans

    def canMake(self, bloomDay, m, k, day):
        """
        检查在第 'day' 天，能否做出 m 束花
        贪心：遍历数组，找连续的 k 朵已开的花
        """
        bouquets = 0  # 已做出的花束数
        flowers = 0  # 当前连续已开的花数

        for bloom in bloomDay:
            if bloom <= day:
                # 这朵花已开
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0  # 用完这 k 朵，重新开始计数
            else:
                # 这朵花未开，连续性中断
                flowers = 0

        return bouquets >= m

s=Solution()
print(s.minDays([1,10,3,10,2],3,1))


"""
总复杂度 = 二分次数 × 每次检查
        = O(log(maxDay)) × O(n)
        = O(n log(maxDay))
"""