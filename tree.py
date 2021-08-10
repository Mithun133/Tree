# Implementing a Tree
"""
            4
          /   \
        5       6
       / \       \
      1   7       9
         / \     / \
        3  10   2   8
    Left | Node | Right
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node
    
    def add_right(self, node):
        self.right = node

def create_tree():
    four = Node(4)
    five = Node(5)
    six = Node(6)
    four.add_left(five)
    four.add_right(six)

    one = Node(1)
    seven = Node(7)
    five.add_left(one)
    five.add_right(seven)

    three = Node(3)
    ten = Node(10)
    seven.add_left(three)
    seven.add_right(ten)

    nine = Node(9)
    six.add_right(nine)

    two = Node(2)
    eight = Node(8)
    nine.add_left(two)
    nine.add_right(eight)

    return four

def pre_order(node):
    print(node.data, end=' ')
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)
    
def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.data, end=' ')

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node.data, end=' ')
    if node.right:
        in_order(node.right)

if __name__ == '__main__':
    tree = create_tree()
    print(tree.data)
    print('\n*Pre_order')
    pre_order(tree)

    print('\n\n*post_order')
    post_order(tree)

    print('\n\n*In_order')
    in_order(tree)
