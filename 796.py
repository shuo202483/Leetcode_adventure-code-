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





def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)

原理: s + s 包含了 s 的所有可能的旋转形式
例如 s = "abcde", s + s = "abcdeabcde"
所有旋转: "abcde", "bcdea", "cdeab", "deabc", "eabcd" 都作为子串出现在其中
