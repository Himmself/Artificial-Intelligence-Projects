class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Reject Data that is already inserted
        if self.data == data:
            print("Already inserted: " + str(data))
        # If incoming data is greater
        elif self.data < data:
            print("Right Insert")
            if self.right == None:
                self.right = Node(data)
            else:
                self = self.right.insert(data)
        # If incoming data is lesser  
        elif self.data > data:
            print("Right Insert")
            if self.left == None:
                self.left = Node(data)
            else:
                self = self.left.insert(data)
        

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node(10)
root.insert(11)
root.insert(12)
root.insert(15)
root.insert(1)
root.insert(12)
root.insert(11)
root.insert(45)
root.insert(4)
root.insert(9)
root.insert(2)

root.PrintTree()