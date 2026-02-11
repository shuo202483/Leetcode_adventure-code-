import heapq

class Solution:
    def lastStoneWeight(self, stones:[int]) -> int:
        #python支持最小堆如果需要最大堆那么需要把数字倒过来
        h=[-x for x in stones]
        heapq.heapify(h)

        while len(h)>1:
            y=heapq.heappop(h)
            x=heapq.heappop(h)
            if y!=x:
                #为了得到实际石头重量之差我们再负一次，这里的运算是先计算括号内的值
                heapq.heappush(h,-(y-x))

        return -h[0] if h else 0

s=Solution()

print(s.lastStoneWeight([2,7,4,1,8,1]))
