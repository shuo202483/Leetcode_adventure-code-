class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        max_area = 0
        stack = []
        # 末尾哨兵，遇到极端情况
        heights = heights + [0]
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # 算宽度时如果没有左边界 i - (-1) - 1 = i，正好覆盖 0 到 i-1 这一段。
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area

s=Solution()
print(s.largestRectangleArea([2,4]))

"""
首先，面积最大矩形的高度一定是 heights 中的元素。这可以用反证法证明：
假如高度不在 heights 中，比如 4，那我们可以增加高度直到触及某根柱子的顶部，比如增加到 5，
由于矩形底边长不变，高度增加，我们得到了面积更大的矩形，矛盾，所以面积最大矩形的高度一定是 heights 中的元素。

枚举每个 h=heights[i]，作为矩形的高。那么矩形的宽最大是多少？我们需要知道：

在 i 左侧的小于 h 的最近元素的下标 left，如果不存在则为 −1。求出了 left，那么 left+1 就是矩形最左边那根柱子。
如果 left=−1，那么加一后是 0，就是整个 heights 最左边的柱子。
在 i 右侧的小于 h 的最近元素的下标 right，如果不存在则为 n。求出了 right，那么 right−1 就是矩形最右边那根柱子。
如果 right=n，那么减一后是 n−1，就是整个 heights 最右边的柱子。
于是宽度
= 右 − 左 + 1
= (i − 1) − (left + 1) + 1
= i − left − 1
从整数 a 到整数 b（含两端）共有 b − a + 1 个数
利用“递增”这一不变式，让每一根柱子在被弹出的一瞬间，恰好知道了自己能向左、向右延伸多远。


考虑两个极端情况：【5】、【1，2，3，4】这些数据都有个共性就是程序运行进栈后没碰到右边界就再也不出栈了
heights = heights + [0]：# 使得所有真正的柱子都必然遇到一个比自己矮的右边界，从而一个不漏地结算面积

"""