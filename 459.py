class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        #最长公共前后缀
        next=[0]*n


        for i in range(1,n):  # # i：当前要处理的字符位置
            j=next[i-1]    #j 已匹配长度，又是下一个要比的索引
            while j>0 and s[i]!=s[j]:
                j=next[j-1]
            if s[i]==s[j]:
                next[i]=j+1

        """
        如果字符串 s 由子串 t 重复 k 次构成，那么：
        s = t + t + ... + t（k次）
        s 的最长相等前后缀长度 = n - |t|
        因此 |t| = n - next[-1]
        只要 n % (n - next[-1]) == 0，就是周期串
        """
        return next[-1] > 0 and n % (n - next[-1]) == 0


s=Solution()
print(s.repeatedSubstringPattern("aabab"))

"""
前缀和后缀不能是字符串本身（否则任何字符串的前后缀都是它自己，没意义）
所以单个字符的 next[0] 只能是 0
因此我们从 i=1（第二个字符）开始计算。

如果相等
上一轮 i=2（"aba"）：next[2]=1，表示有 "a"="a"
这轮 i=3（"abab"）：j=1
                   比较 s[3] 和 s[1]（因为 j=1，下一个该比第1位）
                   'b' == 'b'？是！所以长度可以变成 2
                   next[3] = 2
                   
不相等比较困难
你在计算 next[i]，却要用 next[j-1]，而 j 本身又依赖于之前的 next 值。
这就像："为了知道今天的答案，你要先回答昨天的某个问题，而那个问题的答案又依赖于前天..." （类似于动态规划，不断递推）

比如拿aba这个公共前后缀来说
因为前缀a=后缀a
所以下一次比较就可以省去这两个，从b开始比较
如果字符串长一点比如aabcaabd，遇到不同的时候则可以直接从这个c开始比较，这都是公共前后缀所带来的特性，也就是退到失败匹配前一个字符的最大匹配位置索引上去
"""