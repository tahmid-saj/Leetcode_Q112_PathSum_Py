# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None: return False
        if root.left == None and root.right == None and root.val == targetSum: return True
        if root.left == None and root.right == None and root.val != targetSum: return False

        def helper(node, totalSum):
            if node == None: return
            else:
                if helper(node.left, totalSum + node.val) == True: return True
                if helper(node.right, totalSum + node.val) == True: return True

            if node.left == None and node.right == None and totalSum + node.val == targetSum: return True
            return False
        
        return helper(root, 0)
            
