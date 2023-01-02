import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]


def preOrder(curr):
    if curr != '.':
        print(curr, end='')  # current node
        preOrder(tree[curr][0])  # left node
        preOrder(tree[curr][1])  # right node


def inOrder(curr):
    if curr != '.':
        inOrder(tree[curr][0])  # left node
        print(curr, end='')  # current node
        inOrder(tree[curr][1])  # right node


def postOrder(curr):
    if curr != '.':
        postOrder(tree[curr][0])  # left node
        postOrder(tree[curr][1])  # right node
        print(curr, end='')  # current node


preOrder('A')  # initial node is 'A'
print()
inOrder('A')
print()
postOrder('A')
