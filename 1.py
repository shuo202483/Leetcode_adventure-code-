class Solution:
    def twoSum(self, nums, target):
        co = {}

        for i,num in enumerate(nums):
            complete=target-nums[i]

            #检查补数是否出现过，如果出现则返回索引
            if complete in co:
                return [co[complete],i]
            co[num]=i
        return []


s=Solution()
print(s.twoSum([2,4],6))