class Solution:
    def search(self, nums, target: int) -> int:
        left = 0   #左闭
        right = len(nums)  #右开

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # 左半边有序
            #先确定哪边有序，再判断target是否在这个有序区间内
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                    #如果不在此区间内，转到另一个子区间
                else:
                    left = mid+1
            # 右半边有序
            else:
                if nums[mid] < target <= nums[right-1]:
                    left = mid+1
                else:
                    right = mid
        return -1

s=Solution()
print(s.search([2,1],1))

"""
这一题虽然数组被反转后扭曲其有序性
但如果当前区间 [left, right) 是跨越了两端有序子区间的，那么中间点 mid 总会把当前区间 [left, right] 分成两段，
一段是有序的，一段是无序的
如果 nums[mid] > nums[left]，肯定是左半区间有序；
如果 nums[mid] < nums[right-1]，肯定是右半区间有序
上面找到有序区间只是为了方便我们使用二分法，target也可能在另一个子区间里头
"""