from binarytree import RootNode as root
from binarytree import InsertNode as insert

class Search(insert.Insert):
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Search(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Search(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')


if __name__ == '__main__':
    root = Search(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    print(root.findval(7))
    print(root.findval(14))