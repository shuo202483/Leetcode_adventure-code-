class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        # 基础情况
        if n == 1:
            return [1]

        # 分治：分别构造奇数部分和偶数部分
        # 奇数部分需要 (n+1)//2 个数（1,3,5...）
        # 偶数部分需要 n//2 个数（2,4,6...）
        odds = self.beautifulArray((n + 1) // 2)  # 奇数位置(向上取整)
        evens = self.beautifulArray(n // 2)  # 偶数位置

        # 映射变换
        # 奇数部分：x -> 2x-1 (1,3,5,7...)
        # 偶数部分：x -> 2x   (2,4,6,8...)
        return [2 * x - 1 for x in odds] + [2 * x for x in evens]


s=Solution()
print(s.beautifulArray(2))

"""
等差数列的形成条件：三个数 a, b, c 满足 a + c = 2b，即 b 是 a 和 c 的平均值
漂亮数组就是要避免任何这样的三元组出现在数组中

这道题思路是这么回事:
1、首先观察题目：要求2*k ！= i+j;任何数*2都是偶数，2*k也成立;
也就是说i和j相加不能等于偶数，那么只有i和j一个为奇数一个为偶数的时候才能满足这个条件(i和j全为奇偶也能部分满足，但我们不考虑)

2、所以我们构造一个左边全是奇数的数组和右边全是偶数的数组使得任意的i(奇数组)和j(偶数组)相加永远不等于k即可
至于基础情况就是n=1，或者n=【1，2】#根据前面的情况推导而来
"""