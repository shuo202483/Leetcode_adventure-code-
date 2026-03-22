class Solution(object):
    def threeSumClosest(self,nums, target):
        nums.sort()  # 排序
        n = len(nums)
        # 初始化为前三个数的和（任意三个数都行）
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):  # 固定第一个数
            left, right = i + 1, n - 1  # 双指针

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # 直接命中，返回即可
                if current_sum == target:
                    return current_sum

                # 更新最接近的结果（比较绝对值距离）
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # 移动指针
                if current_sum < target:
                    left += 1  # 和太小，左指针右移增大
                else:
                    right -= 1  # 和太大，右指针左移减小

        return closest


#三树之和
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # 【去重1】跳过重复的 nums[i],不设置大于0可能会导致遗漏元素(考虑全0)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 剪枝：如果当前最小和都大于0，后面不可能有解了
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            # 剪枝：如果当前最大和都小于0，后面不可能有解了
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            left, right = i + 1, n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 【去重2】找到解后，跳过重复的 left 和 right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 必须同时收缩，否则死循环(也就是移动到l和r第一个不同的元素)
                    left += 1
                    right -= 1

                if cur_sum>0:
                    right-=1
                else:
                    left-=1

        return res



s=Solution()
print(s.threeSum([-100,-70,-60,110,120,130,160]))