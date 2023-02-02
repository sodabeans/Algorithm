# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        if curr is None:
            return TreeNode(val)
        while curr:
            if curr.val > val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root
