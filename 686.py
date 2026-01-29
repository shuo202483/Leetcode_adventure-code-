class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 数学计算需要重复几次才能让长度 >= len(b)
        cnt = (len(b) + len(a) - 1) // len(a)  # 向上取整
        
        c = a * cnt
        if b in c:
            return cnt
        
        # 再试一次（跨边界情况，在无限重复的字符串 aaaa... 中，如果 b 是子串，它一定会在前 cnt + 1 个周期内出现）
        if b in c + a:
            return cnt + 1
        
        return -1