# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 1
        self.dfs(root)
        return self.ans - 1
    
    def dfs(self, node):
        if not node: return 0

        L = self.dfs(node.left)
        R = self.dfs(node.right)
        self.ans = max(self.ans, L+R+1)
        return max(L,R)+1