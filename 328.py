# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next: return head

        odd=head   
        even=head.next     #指针只占O(1)的空间
        even_head=even     #保存偶链表头,最后需要接回去

        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next

        odd.next=even_head
        return head

def print_list(head):
    while head:
        print(head.val,end="->")
        head=head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("原始链表:")
print_list(head)

sol = Solution()
new_head = sol.oddEvenList(head)

print("奇偶重排后:")
print_list(new_head)
