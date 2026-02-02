import heapq
class Solution:
    def eatenApples(self, apples, days):
        h=[]
        res=0
        i=0
        n=len(apples)

        while i<n or h:  #还有新苹果要长，或堆里的苹果保质期还在
            if i<n and apples[i]>0:   #也可能存在树上不长苹果的日子
                expire=i+days[i]
                heapq.heappush(h,[expire,apples[i]])  #入栈

            # 清理已经腐烂的（堆顶过期时间 <= 当前天数
            while h and h[0][0]<=i:
                heapq.heappop(h)

            #吃一个：从最快过期的那批里拿一个
            if h:
                res+=1
                h[0][1]-=1
                if h[0][1]==0:
                    heapq.heappop(h)
            i+=1

        return res

s=Solution()
print(s.eatenApples([1,2,3,5,2],[3,2,1,4,2]))
