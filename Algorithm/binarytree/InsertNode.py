from binarytree import RootNode as root

class Insert(root.Node):
    # Compare the new value with the parent node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Insert(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Insert(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


if __name__ == '__main__':
    # Use the insert method to add nodes
    root = Insert(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)

    root.PrintTree()