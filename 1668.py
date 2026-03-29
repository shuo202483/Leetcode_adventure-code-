class Solution(object):
# ========== 方法一：暴力枚举（从大到小） ==========
    def maxRepeating_max_k(self, sequence, word):
        """
        思路：先算理论最大次数 max_k = len(sequence) // len(word)
        从 max_k 往 1 枚举，构造 word*k，第一个在 sequence 里的就是答案
        时间：O(max_k * n * m)  空间：O(m * max_k) 构造字符串的开销
        """
        max_k = len(sequence) // len(word)

        for k in range(max_k, 0, -1):
            # 构造重复 k 次的字符串
            target = word * k
            if target in sequence:
                return k
        return 0
# ========== 方法二：双指针线性扫描 ==========
    def maxRepeating_two_pointers(self, sequence, word):
        """
        思路：枚举每个起始位置，能匹配 word 就跳 len(word) 继续，否则跳 1 换起点
        关键：必须记录"从当前起点开始"的连续次数，失配就换起点清零
        时间：O(n * m)  空间：O(1) 或 O(m)（切片比较时创建子串）
        """
        n, m = len(sequence), len(word)
        max_cnt = 0

        for start in range(n):
            cnt = 0
            i = start
            # 从 start 开始，能连续匹配多少次 word
            while i + m <= n and sequence[i:i + m] == word:
                cnt += 1
                i += m  # 跳过整个 word，检查后面是否还是 word

            max_cnt = max(max_cnt, cnt)

        return max_cnt
# ========== 方法三:优雅的做法 ==========
    def maxRepeating_elegant(self, s, w):
        k = 0
        while w * (k + 1) in s:
            k += 1
        return k
# ========== 方法四：KMP ==========
    def maxRepeating_kmp(self, sequence, word):
        m = len(word)
        # LPS
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j and word[i] != word[j]:
                j = lps[j - 1]
            if word[i] == word[j]:
                j += 1
                lps[i] = j

        # 匹配，dp[i] = 以位置 i 结尾的连续重复次数
        n = len(sequence)
        dp = [0] * n
        j = 0
        for i, ch in enumerate(sequence):
            while j and ch != word[j]:
                j = lps[j - 1]
            if ch == word[j]:
                j += 1
            if j == m:  # 匹配完，这个 word 结尾在位置 i
                dp[i] = (dp[i - m] if i >= m else 0) + 1
                #防止越界和利用已知信息避免重复比较
                j = lps[j - 1]
        return max(dp) if dp else 0



