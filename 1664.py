class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        #得到奇偶的总和
        total_even = sum(nums[i] for i in range(0, n, 2))
        total_odd = sum(nums[i] for i in range(1, n, 2))

        #当前位置的奇偶前缀和
        left_even = 0
        left_odd = 0
        res = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                #删除当前元素后的奇偶前缀和
                #这里不用减去num是因为total_odd本身就不包含偶数
                new_even = left_even + (total_odd - left_odd)
                #当前元素 nums[i] 被删除了，它不属于"左边"，也不属于"右边"，必须从总和中彻底剔除
                new_odd = left_odd + (total_even - left_even - num)
                if new_even == new_odd:
                    res += 1
                left_even += num
            else:
                #同上
                new_even = left_even + (total_odd - left_odd - num)
                new_odd = left_odd + (total_even - left_even)
                if new_even == new_odd:
                    res += 1
                left_odd += num
        return res

s=Solution()
print(s.waysToMakeFair([2,1,6,4]))

"""
| 部分          | 奇偶性    | 贡献到新偶数和 | 贡献到新奇数和 |
| 左边（0~i-1）   | 不变     | 原偶数位    | 原奇数位    |
| 右边（i+1~n-1） | **翻转** | 原奇数位    | 原偶数位    |
新偶数和 = 左边偶数 + 右边原奇数
新奇数和 = 左边奇数 + 右边原偶数

核心:左偶+右原奇=左奇+右原偶
"""