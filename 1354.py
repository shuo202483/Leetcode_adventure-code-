import heapq

class Solution:
    def isPossible(self, target):
        #获得总和
        total=sum(target)

        #建立最大堆
        max_heap=[-x for x in target]
        heapq.heapify(max_heap)

        #只要最大值大于1就继续拆
        while -max_heap[0]>1:
            #当前的最大值
            cur=-heapq.heappop(max_heap)
            #rest是旧值
            rest=total-cur

            #根据下方推论想要保证继续逆推，那么必须满足最大值大于剩余元素(不然结果为0，这与全1数组违背)
            if rest==0 or cur<=rest:
                return False
            #见下方
            old=(cur-1)%rest+1
            #根据推论得到
            total=rest+old
            heapq.heappush(max_heap,-old)

        return True

s=Solution()
print(s.isPossible([9,3,5]))

"""
逆向：从 target 出发，每轮把当前最大值还原成“上一轮”的旧值。
旧值 = 最大值 – (其余元素之和)
而“其余元素之和”就是 总和 – 最大值，所以我们必须知道当前的总和。

这道题的数组范围最高是10^9次方法，正常的判断方法是old=cur-rest，但是明显时间会超出
但是我们不难发现这其实等同于cur%rest(一遍一遍的减正好是求余)

我们做了一些偏移，首先减去1,此时old在[0,rest-1]区间内，再加上1，使其永远在区间[1,rest]
如果直接cur%rest可能会得到0，这不符合题意
"""