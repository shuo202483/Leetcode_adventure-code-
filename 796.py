class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 长度检查可以加上，避免无谓的循环
        if len(s) != len(goal):
            return False
            
        for i in range(len(s)):
            s = s[1:] + s[0]  # 模拟左旋一位
            if s == goal:
                return True
        return False

时间复杂度: O(n²) — 每次切片 s[1:] + s[0] 都是 O(n) 的操作，循环 n 次
空间复杂度: O(n) — 每次切片都创建新字符串


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        s = s * 2
        n, m = len(s), len(goal)

        # 计算 pi 数组
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and goal[j] != goal[i]:
                j = pi[j - 1]
            if goal[j] == goal[i]:
                pi[i] = j + 1

        # KMP 匹配
        j = 0    #j是要比较的下标也是最长的长度
        for i in range(n):
            while j > 0 and goal[j] != s[i]:
                j = pi[j - 1]
            if j < m and goal[j] == s[i]:
                j += 1
            if j == m:
                return True
        return False


"s + s 包含了所有可能的旋转形式，所以问题转化为：goal 是否是 s+s 的子串？"
"构造一个包含所有候选的母串，然后用高效算法匹配。下次遇到循环/旋转/重复类问题，可以往这个方向想"


def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)

原理: s + s 包含了 s 的所有可能的旋转形式
例如 s = "abcde", s + s = "abcdeabcde"
所有旋转: "abcde", "bcdea", "cdeab", "deabc", "eabcd" 都作为子串出现在其中

