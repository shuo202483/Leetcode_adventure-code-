class Solution:
    def minSubarray(self, nums, p: int) -> int:
        total = sum(nums)
        target = total % p

        #刚好
        if target == 0:
            return 0

        #key是前缀余数、value余数出现的第一次索引,0:-1是个虚拟节点，用来返回i+1(i-(-1)),即刚好这个点的长度
        prefix_map = {0: -1}
        cur_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            #当前前缀
            cur_sum = (cur_sum + num) % p
            #查看当前前缀的余数是否存在
            need = (cur_sum - target) % p
            if need in prefix_map:
                min_len = min(min_len, i - prefix_map[need])
            prefix_map[cur_sum] = i

        return -1 if min_len == len(nums) else min_len

s=Solution()
print(s.minSubarray([6,3,5,2],9))

"""
这道题可以观察到target总是等于total%p
前缀和把"子数组和"变成"两个前缀相减"，哈希表把"找另一个前缀"变成 O(1)

哈希表作用:
(cur_sum + num) % p  →  保证 cur_sum ∈ [0, p-1] 
必须每轮取余，因为哈希表要在每个位置记录 prefix[j] % p，不求余没法保证cur_sum能在哈希表中查到(数学推理上可以不取，但是实际程序可能会溢出)


子数组[i+1..j]的和 = prefix[j](终点) - prefix[i]（起点）
我们需要：(prefix[j] - prefix[i]) % p = target

两边同时 % p（性质不变）：
(prefix[j] % p - prefix[i] % p) % p = target % p
因为 target = total % p，所以 target % p = target

设 cur_sum = prefix[j] % p，need = prefix[i] % p：
(cur_sum - need) % p = target

cur_sum - need ≡ target (mod p)
移项：
need ≡ cur_sum - target (mod p)
所以：
need = (cur_sum - target) % p

"""