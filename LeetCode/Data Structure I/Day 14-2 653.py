# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        values = []
        def search(node, k):
            if node == None:
                return False
            if k - node.val in values:
                return True
            values.append(node.val)
            return search(node.left, k) or search(node.right, k)
        return search(root, k)
