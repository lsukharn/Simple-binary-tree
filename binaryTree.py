#Simple binary tree implementation

#Creates a Node object without children
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Creates a Tree object 
class Tree:
    def __init__(self):
        #start with an empty root
        self.root = None
    
    #Add method checks if the tree is empty
    #if it's empty it creates its root
    #if not (root exists) then it will start traversing the tree with _add
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)
    
    #Traversing the tree
    def _add(self, value, node):
        #to satisfy the binary tree condition _add checks whether the new value 
        #is bigger or smaller than the current node's value
        if value < node.value:
            #if no left child -> create a left child with value and exit
            #else traverse to the left recursively
            if node.left == None:
                node.left = Node(value)
            else:
                self._add(value, node.left)
        else:
            #similar logic for the right child
            if node.right == None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def find(self, value):
        if self.root != None:
            self._find(value, self.root)
    
    #Perform a tree traversal to find a node with a given value
    def _find(self, value, node):
        if node.value == value:
            print "found node with value: %s" % node.value
        elif value < node.value and node.left != None:
            self._find(value, node.left)
        elif value > node.value and node.right != None:
            self._find(value, node.right)
        else:
            print "No node with value: %s" % value
    
    def deleteTree(self):
        self.root = None
    
    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
    
    #Perform inOrderTraversal to print tree
    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print '\t%s' % node.value
            self._printTree(node.right)

def main():
    t1 = Tree()
    t1.add(5)
    t1.add(10)
    t1.add(3)
    t1.add(100)
    t1.find(100)
    t1.find(3)
    t1.find(6)
    t1.printTree()

if __name__ == "__main__":
    main()
        
        
