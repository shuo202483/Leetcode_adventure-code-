class Solution:
    def removeDuplicateLetters(self, s: str):
        last = {ch: idx for idx, ch in enumerate(s)}

        stack=[]
        for i in range(len(s)):
            if s[i] in stack: continue
                                                       #如果后面还有值
            while stack and stack[-1]>s[i] and last[stack[-1]]>i:
                stack.pop()
            stack.append(s[i])

        return "".join(stack)

s=Solution()
print(s.removeDuplicateLetters("cbacdcbc"))



这个问题需要注意一段关键字：相对顺序不变的情况下找到最小字典序，也就是说在去重完后原始字符中后面的字符不会提前到前面去(可以保证我们统计每个字符的最后位置)


