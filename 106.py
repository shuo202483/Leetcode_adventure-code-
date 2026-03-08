#关于二叉树的遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result

#正式代码
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        #后序数组节点
        root_val=postorder[-1]
        root=TreeNode(root_val)
        #获得当前根节点左右两边的数量
        idx=inorder.index(root_val)
        left_size=idx

        root.left=self.buildTree(inorder[0:idx],postorder[0:left_size])
        root.right=self.buildTree(inorder[idx+1:],postorder[left_size:-1])

        return root

s=Solution()
print(s.buildTree([9,3,15,20,7],[9,15,7,20,3]))



"""
分治算法需要找到一个中间值然后不断左右分裂，再根据子问题合并得到大问题
观察这道题我们会发现:
后序数组的最后一个值永远是当前子树的根节点，通过这个值我们就可以找到其在中序数组中的左右节点的数量
不断的递归，直至找到最后一个节点为止，开始返回合并，构造出这个二叉树
"""