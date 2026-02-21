class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid]==target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid+1

        return -1
