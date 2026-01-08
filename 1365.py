#排序+二分查找
from bisect import bisect_left, bisect_right


class Solution:
    def smallerNumbersThanCurrent(self, nums):   # 注意 self
        sorted_nums = sorted(nums)
        return [bisect_right(sorted_nums, x) for x in nums]
from bisect import bisect_left

#bisect库的效果
a = [1, 2, 2, 3, 8]          # 已排好序
tests = [0, 1, 2, 3, 5, 8, 9]

for x in tests:
    pos = bisect_left(a, x)
    smaller = a[:pos]        # 真正比 x 小的那些元素
    print(f'x={x:2}  插入位置={pos}  比它小的元素={smaller}')
"""
这个库left和right都是查找整个数组，唯一的区别在于right还包括等于自己的值
"""

#前缀计数
class Solution:
    def smallerNumbersThanCurrent(self, nums:[int]) -> [int]:
        out=[]
        count=[0]*101

        for i in nums:
            count[i]+=1

        min_num=[]
        temp=0
        for i in count:
            min_num.append(temp)
            temp+=i

        for i in nums:
            out.append(min_num[i])


        return out