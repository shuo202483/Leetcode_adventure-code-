#快速选择
import random
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中

            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)

            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if k > len(big) + len(equal):
                return quick_select(small, k - len(big) - len(equal))

            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quick_select(nums, k)

"这个做法来自leetcode的Krahets，非本人原创"
s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))


#堆
import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        min_heap=[]
        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap)>k:
                heapq.heappop(min_heap)   # 弹出最小的，保留 k 个大的
        return min_heap[0]


s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))  # 堆顶就是第 k 大的

"""
时间O(nlogk)	   堆大小最多k，总共操作n个元素
空间O(k)
海量数据、数组不可修改
最大堆时间复杂度会更高

但这些场景堆更优：
内存只有 1GB，数据有 100GB（外部排序/Top K）
数据流实时进来（在线算法）
不能修改原数组（只读数据）
所以面试常问："如果数据流/内存不够怎么办？" 就是在考察你能不能想到堆的解法
"""

#传统快速选择方法
import random
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]

            # pivot放右边
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # 小的扔左边
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            # pivot归位[回位后左边只小不大	✓但无序，所以叫"快速选择"不是"快速排序"]
            nums[right], nums[store_idx] = nums[store_idx], nums[right]

            # 只走一边
            if store_idx == k:
                return nums[k]
            elif store_idx < k:
                left = store_idx + 1
            else:
                right = store_idx - 1

        return nums[left]

s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))
"""
放最右边 = 物理隔离，左边遍历完全不管 pivot，最后 swap 回来，保证：
左边全是 < pivot
归位后左边 < pivot < 右边
"""