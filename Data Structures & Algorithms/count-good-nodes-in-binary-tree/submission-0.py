# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(greatest_value , root):
            if not root:
                return 
            
            if root.val >= greatest_value:
                res[0]+=1
            
            greatest_value = max(root.val,greatest_value)
            
            dfs(greatest_value,root.left)
            dfs(greatest_value,root.right)

        dfs(root.val,root)
        return res[0]

            