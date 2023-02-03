# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def search(node, minimum, maximum):
            if node == None:
                return True
            elif node.val >= maximum or node.val <= minimum:
                return False
            else:
                return search(node.left, minimum, node.val) and search(node.right, node.val, maximum)

        return search(root, -(10e10), (10e10))
