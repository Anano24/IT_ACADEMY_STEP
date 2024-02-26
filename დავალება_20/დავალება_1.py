# მოიძიეთ ინფორმაცია ბინარულ ხეზე და დაწერეთ დაბეჭდვის ფუნქციები printLeafNodes და countEdges



# This class represents a single node in a binary tree.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


# This class represents a binary tree data structure.
class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self, key):
        self.root = self._insert(self.root, key)


    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node
    


    def print_parents(self):
        print("The parents are: ")
        self._print_parents(self.root, None)


    def _print_parents(self, node, parent):
        if node is not None:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)



    def print_children(self):
        print("Printing children Nodes:")
        self._print_children(self.root)


    def _print_children(self, node):
        if node is not None:
            print(node.key, "-> ", end="")
            if node.left is not None:
                print(node.left.key, "-> ", end="")
            if node.right is not None:
                print(node.right.key, "-> ", end="")
                
            print()

            self._print_children(node.left)
            self._print_children(node.right)



    def print_leaf_nodes(self):
        print("Leaf Nodes:")
        self._print_leaf_nodes(self.root)


    def _print_leaf_nodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.key)
            self._print_leaf_nodes(node.left)
            self._print_leaf_nodes(node.right)



    def count_edges(self):
        if self.root is None:
            return 0
        return self._count_edges(self.root) - 1  # Subtracting 1 because number of edges = number of nodes - 1


    def _count_edges(self, node):
        if node is None:
            return 0
        return 1 + self._count_edges(node.left) + self._count_edges(node.right)


    
        

binary = BinaryTree()

binary.insert(5)
binary.insert(3)
binary.insert(9)
binary.insert(2)
binary.insert(4)
binary.insert(1)
binary.insert(8)
binary.insert(10)
binary.insert(11)
binary.insert(7)
binary.insert(56)
binary.insert(30)

binary.print_parents()
binary.print_children()
binary.print_leaf_nodes()
print("Number of Edges:", binary.count_edges())

    
