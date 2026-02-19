"""
将唯一值按从小到大排序后，设排序后的唯一值为 arr[0], arr[1], ..., arr[m-1]：
arr[0]（最小值）不需要操作
arr[1] 需要 1 层操作（降到最小值）
arr[2] 需要 2 层操作
arr[i] 需要 i 层操作
所以总操作次数 = Σ (count[arr[i]] × i)，其中 i 是该值在排序后唯一值数组中的下标（从0开始，但最小值下标为0，贡献为0）。

| 方案       | 时间         | 空间            | 核心操作              |
| -------- | ---------- | ------------- | ----------------- |
| **用哈希**  | O(n log n) | O(n)          | 排序 + 哈希统计 + 遍历唯一值 |
| **不用哈希** | O(n log n) | **O(1)** 额外空间 | 排序 + 一次遍历         |

"""
class Solution:
    def reductionOperations(self, nums) -> int:
        nums.sort()    #nlogn
        hash={}
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1

        k=1
        res=0
        for i in hash:
            if i!=nums[0]:
                res+=k*hash[i]
                k+=1

        return res


s=Solution()
print(s.reductionOperations([1,1,2,2,3]))


class Solution:
    def reductionOperations(self, nums) -> int:
        nums.sort()
        res = 0
        level = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # 遇到新唯一值
                level += 1
            res += level  # 当前元素需要 level 次操作

        return res