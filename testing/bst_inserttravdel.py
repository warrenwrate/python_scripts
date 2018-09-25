class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
class BST:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, root, value):

        if self.root is None:
            self.root = Node(value)

        if root is None:
            return Node(value) 
        
        if root.value >= value:
            root.left = self.insert(root.left, value)
        if root.value < value:
            root.right = self.insert(root.right, value)

        return root

    def find(self, root, value):
        #pass
        if root == value:
            return root
        if root is None:
            raise Exception('Cannot find value in tree')
            return None

        if root.value > value:
           return self.find(root.left, value)
        
        if root.value < value:
            return self.find(root.right, value)

        return root

    def min_node(self, root):
        while root.left:
            return self.min_node(root.left)
        return root


    def delete(self, root, value):
       
        if root is None:
            raise Exception('Cannot find value to delete')

        if root.value > value:
            root.left = self.delete(root.left, value)

        elif root.value < value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = self.min_node(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)
        return root



bst = BST()
bst.insert(bst.root, 15)
bst.insert(bst.root, 10)
bst.insert(bst.root, 7)
bst.insert(bst.root, 8)
bst.insert(bst.root, 5)
bst.insert(bst.root, 12)
bst.insert(bst.root, 30)
bst.insert(bst.root, 40)
bst.insert(bst.root, 35)
found = bst.find(bst.root, 12)
min_value = bst.min_node(bst.root)

print('found:',found.value)
print('min_value:',min_value.value)
bst.delete(bst.root, 7)
print('done')
pass

