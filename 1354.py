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

如果最大值 x=100，但其余元素之和只有 sum=3，那么 100−3=97，由于 97>3，新得到的数字 97 比其余元素之和还要大，必然还是 target 的最大值。我们会把这个最大值反复地减去 3，直到 ≤3 为止。
当 cur 远大于 rest 时（比如 [1000000000, 1]），一步步减法太慢，所以用取模批量处理：cur % rest


不能减成 0 或者负数，我们做了一些偏移，首先减去1,此时old在[0,rest-1]区间内，再加上1，使其永远在区间[1,rest]
如果直接cur%rest可能会得到0，这不符合题意

"""
