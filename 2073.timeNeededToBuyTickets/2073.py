class Solution:
    def timeRequiredToBuy(self, tickets, k):
        target = tickets[k]
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)

        return time

s=Solution()
print(s.timeRequiredToBuy([2,3,2],2))
# print(s.timeRequiredToBuy([5,1,1,1],0))