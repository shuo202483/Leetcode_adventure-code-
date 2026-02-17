class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head):
        #先将链表转换成数组，因为数组支持随机访问
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next

        n=len(nums)
        #根据题目定义，不存在比自身大的数都为0
        answer=n*[0]
        stack=[]

        #这里就是简单的单调栈
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                idx=stack.pop()
                answer[idx]=nums[i]
            stack.append(i)

        return answer

header=ListNode(9,ListNode(7,ListNode(6,ListNode(7,ListNode(6,ListNode(9))))))
s=Solution()
print(s.nextLargerNodes(header))