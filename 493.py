class Solution:
    def reversePairs(self, nums):
        self.nums = nums
        return self.merge_sort(0, len(nums) - 1)

    """
    merge_sort:
    左边和右边都已经排好了，看看左边哪些数>右边哪些数的2倍
    """
    def merge_sort(self, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        count = self.merge_sort(l, mid) + self.merge_sort(mid + 1, r)

        # 统计横跨的翻转对
        "这个程序就是在正常的归并排序的基础上添加了这一段代码块"
        j = mid + 1
        for i in range(l, mid + 1):
            while j <= r and self.nums[i] > 2 * self.nums[j]:
                j += 1
            count += j - (mid + 1)

        # 标准归并
        self.merge(l, mid, r)
        return count

    def merge(self, l, mid, r):
        # 临时数组，合并两个有序部分
        temp = []
        i, j = l, mid + 1

        while i <= mid and j <= r:
            if self.nums[i] <= self.nums[j]:
                temp.append(self.nums[i])
                i += 1
            else:
                temp.append(self.nums[j])
                j += 1

        temp.extend(self.nums[i:mid + 1])
        temp.extend(self.nums[j:r + 1])

        # 写回原数组
        self.nums[l:r+1]=temp
        #也可也这么写
        # for idx, val in enumerate(temp):
        #     self.nums[l + idx] = val
        
s=Solution()
print(s.reversePairs([1,3,2,3,1]))

"""
分	把数组切成两半	直到每段只有1个元素
治	合并两个有序段	从小段有序合并成大段有序

递归深度：O(log N)
每层工作量：O(N) 合并
总复杂度：O(N log N)
"""

#这里还有一种使用二分查找的优雅解法哈哈
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb, res = [], 0
        for n in reversed(nums) :
            res += bisect.bisect_left(tb, n)
            n2 = 2*n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res

作者：RockyPan
链接：https://leetcode.cn/problems/reverse-pairs/solutions/335729/zui-jian-dan-yi-shi-xian-de-fang-fa-er-fen-cha-zha/
来源：力扣（LeetCode）
