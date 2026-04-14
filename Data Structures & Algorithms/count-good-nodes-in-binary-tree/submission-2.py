# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        q = deque()
        max_value = root.val
        q.append((root,max_value))

        while q:
            node,max_value= q.popleft()
            
            if node.val >= max_value:
                res+=1
            max_value = max(max_value,node.val)

            if node.left:
                q.append((node.left,max_value))
            if node.right:
                q.append((node.right,max_value))

       
        return res

            