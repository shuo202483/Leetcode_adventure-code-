class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0, head)
        last_sorted = head  # 已排序区的最后一个节点
        curr = head.next  # 待插入的节点

        while curr:
            if curr.val >= last_sorted.val:
                # 直接放尾部，不用动
                last_sorted = last_sorted.next
            else:
                # 需要从头找插入位置
                prev = dummy
                while prev.next.val < curr.val:  # 找第一个 >= curr 的位置
                    prev = prev.next

                # 现在 prev.next 是第一个 >= curr 的节点
                # 1. 摘除 curr
                last_sorted.next = curr.next

                # 2. 插入到 prev 后面
                curr.next = prev.next
                prev.next = curr

            curr = last_sorted.next  # 下一个待插入节点

        return dummy.next

head=ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
s=Solution()
new_head=s.insertionSortList(head)


def print_list(head):
    cur=head
    while cur:
        print(cur.val,end="->")
        cur=cur.next
    print("null")
print_list(new_head)


