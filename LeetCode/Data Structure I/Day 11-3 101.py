# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def symmetry(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None and node2 != None:
                return False
            if node1 != None and node2 == None:
                return False
            if node1.val != node2.val:
                return False
            return symmetry(node1.left, node2.right) and symmetry(node1.right, node2.left)

        return symmetry(root.left, root.right)
