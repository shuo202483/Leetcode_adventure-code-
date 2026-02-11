class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # 旧头部节点已被指向None(第一轮执行cur.next时)
        return pre
"""
当 cur 指向最后一个节点时，cur.next 是 None；
我们先把 nxt = cur.next 这一步只是把 None 存进变量，并没有对 None 做任何解引用,是合法的操作
"""

def print_list(head):
    while head:
        print(head.val,end="->")
        head=head.next
    print("None")

head=ListNode(1,ListNode(2,(ListNode(3))))

print_list(head)
print()

sol = Solution()
new_head = sol.reverseList(head)
print_list(new_head)   # 期待输出 3->2->1->None
