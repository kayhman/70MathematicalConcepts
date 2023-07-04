class DecisionNode:
    # Decision node class.
    # It is a simple binary node, potentially with two children: left and right.
    # The left node is returned when the condition is true.
    # The False node is returned when the condition is false.
    def __init__(self, name, condition, value=None):
        self.name = name
        self.condition = condition
        self.value = value
        self.left = None
        self.right = None

    def add_left_node(self, left):
        self.left = left

    def add_right_node(self, right):
        self.right = right

    def is_leaf(self):
        # A node without children is a leaf
        return (not self.left) and (not self.right)

    def next(self, data):
        # Returns the node to traverse based on the test result
        cond = self.condition(data)
        if cond:
            return self.left
        else:
            return self.right


class DecisionTree:
    # A DecisionTree is a model that provides predictions based on inputs.
    # A prediction is the sum of the values of the leaves that have been activated by the input.
    def __init__(self, root):
        self.root = root

    def predict(self, data):
        child = self.root
        while child and not child.is_leaf():
            child = child.next(data)
        return child.value


root = DecisionNode('root', lambda d : d['A'] > 2.0)
root_left = DecisionNode('root_left', lambda d : d['B'] > 10.0, None)
root_right = DecisionNode('root_right', None, 1)
left_left = DecisionNode('left_left', None, 2)
left_right = DecisionNode('left_right', None, 3)

root.add_left_node(root_left)
root.add_right_node(root_right)

root_left.add_left_node(left_left)
root_left.add_right_node(left_right)

tree = DecisionTree(root)
print(tree.predict({'A' : 1, 'B' : 1})) # 1
print(tree.predict({'A' : 1, 'B' : 10})) # 1
print(tree.predict({'A' : 3, 'B' : 11})) # 2
print(tree.predict({'A' : 3, 'B' : 9})) # 3