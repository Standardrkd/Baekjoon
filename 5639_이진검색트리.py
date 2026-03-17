class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.Right = None
    
class Tree:
    def __init__(self, root):
        self.root = root # root는 Node의 객체

    def insert(self, Node):
        p = self.root
        if p.data < Node.data and p.left == None:
            p.left = Node
        if Node.data < p.data:
            pass

