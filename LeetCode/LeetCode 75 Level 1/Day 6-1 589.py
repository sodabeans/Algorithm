"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        answer = []
        def search(node):
            if node:
                answer.append(node.val)
                if node.children:
                    for c in node.children:
                        search(c)
        search(root)
        return answer
