#堆
import heapq
class Solution:
    def sortArray(self, nums):
        #直接堆化（O(n)）
        h = nums.copy()
        heapq.heapify(h)  
        
        result = []
        # 每次弹出最小值，因为堆本身不负责排序，只保持树结构
        while h:
            result.append(heapq.heappop(h))  
        
        return result

# 测试
s = Solution()
print(s.sortArray([5, 1, 1, 2, 0, 0]))



#计数
class Solution:
    def sortArray(self, nums):
        #这道题数据量不算特别大，但是我们为了避免浪费，可以选择找最值来确定范围
        max_val = max(nums)
        min_val = min(nums)

        offset = -min_val
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num + offset] += 1

        res = []
        for i in range(len(count)):
            while count[i] > 0:
                res.append(i - offset)  # 减去偏移量还原
                count[i] -= 1

        return res

s=Solution()
print(s.sortArray([3,-1]))

"""
这个题目还会出现负数的情况，这个时候可以做一些偏移、
时间：O(n + k)，k 是数值范围
空间：O(k)
"""


#三路排序
import random
class Solution:
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, left, right):
        if left >= right:
            return

        # 随机选pivot
        pivot_idx = random.randint(left, right)
        pivot_val = nums[pivot_idx]

        # 三路分区：lt左边<, gt右边>, 中间=
        lt, gt = left, right  # lt: <pivot的边界, gt: >pivot的边界
        #遍历指针
        i = left

        #核心部分
        while i <= gt:
            if nums[i] < pivot_val:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
                #lt位置一定是已经被处理过的，已知的，所以i可以前进(lt永远小于等于i)
            elif nums[i] > pivot_val:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
                # i 不动，换过来的元素需要再判断
            else:  # == pivot_val
                i += 1

        # 现在 [left, lt-1] < pivot, [lt, gt] == pivot, [gt+1, right] > pivot
        # 只递归两边，中间相等的部分已经有序！
        self.quicksort(nums, left, lt - 1)
        self.quicksort(nums, gt + 1, right)

s=Solution()
print(s.sortArray([5,2,3,1]))


"""
快排遇到全相同元素时会退化到 O(n²),这边考虑三路快排
如果需要改成降序的话只需要改变核心部分的符号

荷兰国旗问题是三路快排的源头，经典算法题！
问题背景
荷兰国旗有三种颜色：🔴 红、⚪ 白、🔵 蓝
给定一个乱序的数组，比如 [蓝, 红, 白, 蓝, 红, 白, 白]，要求原地按 红 < 白 < 蓝 排序。
"""


#归并排序
class Solution:
    def sortArray(self, nums):
        #先分而后合,先把整个数组分到子数组长为1的情况，然后再回溯合并
        if len(nums)<=1:
            return nums

        mid=len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self,left,right):
        res=[]
        i=j=0
        #拉链式比较
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:  # 稳定性：<= 保证相等时左边先出
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1

        "我们不难发现根据while条件至少有一个数组没用完"
        "所以下面等价于res.extend(left[i:] or right[j:]),也可以这么写但是可读性不高"
        #拼接剩余的
        res.extend(left[i:])
        res.extend(right[j:])
        return res

s=Solution()
print(s.sortArray([5,2,3,1]))


"""
时间	O(n log n)	每层O(n)，共log n层
空间	O(n)	需要额外数组存合并结果
稳定性	✅ 稳定(相比于快排) 相等元素相对顺序不变


拉链式比较
左右齿交错咬合	左右数组元素交错放入结果
哪边齿先到位先拉哪边	哪边元素小先放哪边
最终合成一条	最终合成一个有序数组
"""