import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate():
    root = Node(0)
    if random.random() < .5:
        root.left = generate()
    if random.random() < 0.5:
        root.right = generate()

    return root

def getSize(tree):
    if tree == None:
        return 0:
    else return 1 + getSize(tree.left) + getSize(tree.right)
