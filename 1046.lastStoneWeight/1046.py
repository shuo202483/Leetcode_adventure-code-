import heapq

class Solution:
    def lastStoneWeight(self, stones:[int]) -> int:
        h=[-x for x in stones]
        heapq.heapify(h)

        while len(h)>1:
            y=heapq.heappop(h)
            x=heapq.heappop(h)
            if y!=x:
                heapq.heappush(h,-(y-x))

        return -h[0] if h else 0

s=Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))