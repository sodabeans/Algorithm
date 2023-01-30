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
        answer = False
        if root:
            queue = [root]
        else:
            return answer
        while queue:
            curr = queue.pop(0)
            if curr.left != None:
                curr.left.val += curr.val
                queue.append(curr.left)
            if curr.right != None:
                curr.right.val += curr.val
                queue.append(curr.right)
            if curr.left == None and curr.right == None and curr.val == targetSum:
                answer = True
                break
        return answer

