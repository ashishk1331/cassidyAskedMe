from collections import deque


class Node:

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def level_order(self):
        order = []
        q = deque([self])

        while q:
            temp = []

            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            order.append(temp)

        return order

    def depth(self):
        root = self

        def height(root):
            if root:
                left = height(root.left)
                right = height(root.right)

                return 1 + max(left, right)
            return 0

        return height(self)

    def printTree(self):
        height = self.depth()
        width = 2*(height + (height - 1)) - 1

        order = []
        q = deque([self])
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    temp.append(None)
                    continue
                temp.append(node.val)

                q.append(node.left)
                q.append(node.right)
            order.append(temp)

        order.pop()
        counter = 2*height - 1

        for index, each in enumerate(order):
        	if index > 0:
        		sep = "/ \\"
        		separator = " ".join([sep]*index)
        		print(" "*counter, separator)
        		counter -= 1
        	level = (" "*height).join(
        		map(lambda x: " " if x is None else str(x), each))
        	print(" "*counter, level)
        	counter -= 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print(root.level_order())
root.printTree()
