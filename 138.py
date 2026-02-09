class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 第一遍：创建新节点
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 第二遍：连接指针
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)  #这边get到的是值
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]

# ========== 测试 ==========
# 创建链表: 1 -> 2 -> 3
# random:   1->null, 2->1, 3->2

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

node1.random = None
node2.random = node1
node3.random = node2

# 深拷贝
sol = Solution()
new_head = sol.copyRandomList(node1)

# 验证：打印新链表
cur = new_head
while cur:
    random_val = cur.random.val if cur.random else None
    print(f"节点{cur.val}, random指向{random_val}")
    cur = cur.next

# 验证是否是新节点（地址不同）
print(f"原head地址: {id(node1)}")
print(f"新head地址: {id(new_head)}")




#交叉链表
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 复制每个节点，把新节点直接插到原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                # 要复制的 random 是 cur.random 的下一个节点
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 删除交错链表中的原链表节点，剩下的节点即为新链表
        cur = dummy = Node(0, head)
        while cur.next:
            # 跳过源节点
            cur.next = cur.next.next
            cur = cur.next

        return dummy.next


"""需要恢复节点
copy = cur.next          # 1. 拿到新节点（新1）
tail.next = copy         # 2. 新链表接上：tail(0) → 新1
cur.next = copy.next     # 3. 老链表恢复：原1 → 原2
cur = cur.next           # 4. cur走到原2
tail = tail.next         # 5. tail走到新1
"""