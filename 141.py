"以下两种都是hash的做法，只不过第一种改写成了集合的方式,因为这道题有很明显的布尔判断性"
class Solution(object):
    def hasCycle(self, head):
        visited = set()  # 用 set 就行，不需要 dict
        cur = head

        while cur:
            if cur in visited:  # 发现这个节点来过，有环！
                return True
            visited.add(cur)    # 记录这个节点
            cur = cur.next      # 继续走

        return False  # cur 变成 None 了，走到头了，没环

class Solution:
    def hasCycle(self, head) -> bool:
        # 1. python map
        h = {}
        while head:
            if h.get(head):
                return True
            h[head] = 1
            head = head.next
        return False

#双指针(快慢指针)
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        # slow 在 fast 后面，如果 fast 不是空，那么 slow 肯定也不是空
        #即使 fast.next.next 是 None（链表结尾），赋值给 fast 后不会立即访问它，我们只需要确保当前和下一个的fast存在即可，所以是安全的
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

"""
如果当前存在一个环，那么个指针一定都会进入这个环，快指针相对于慢指针每次会多走一次(相对于慢指针不同，快指针追赶它)
那么至多需要L(环的长度)-1次就可相遇
"""
