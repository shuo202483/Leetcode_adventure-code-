"""
这道题有个很关键的观察点：
如果数组长度是 n，那么答案一定在 [1, n+1] 这个范围内
最坏情况：数组里正好装着 1, 2, 3, ..., n，那答案就是 n+1
其他情况：1 到 n 之间肯定有个"洞"，答案就是那个缺的最小正整数
"""


#负数标记法
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # 把非正数和大于n的数变成n+1（垃圾值）
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # 第二步：标记 - 数字k出现，就把下标k-1处的数变负
        for i in range(n):
            num = abs(nums[i])  # 取绝对值，因为可能已经被标记过了(即负数)
            if num <= n:  # 只处理[1,n]范围内的
                nums[num - 1] = -abs(nums[num - 1])

        # 第三步：找第一个正数的位置
        for i in range(n):
            if nums[i] > 0:
                return i + 1  # 下标i对应数字i+1

        return n + 1  # 1~n都在，答案是n+1

s=Solution()
print(s.firstMissingPositive([3,4,-1,1]))


#模拟学生换座位
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 如果当前学生的学号在 [1,n] 中，但（真身）没有坐在正确的座位上(处理发生重复元素的情况)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        # 找第一个学号与座位编号不匹配的学生
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 所有学生都坐在正确的座位上
        return n + 1


s=Solution()
print(s.firstMissingPositive([3,4,-1,1]))