class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        idx = 0
        n = len(tickets)
        # 循环买票
        while tickets[k] != 0:
            if tickets[idx] > 0:
                tickets[idx] -= 1
                ans += 1
            # 下标循环
            idx = (idx + 1) % n
        return ans