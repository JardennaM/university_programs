from node import Node
import math

class BST(object):
    def __init__(self, key_list=[]):
        """Create a new BST, set its attributes, and insert all the keys in
           the key_list into the BST."""
        self.list_of_all_nodes = []
        if not key_list: 
            self.root = None
            self.height = -1
        else:
            self.root = insert(key_list[0])
            self.height = 0
            for key in key_list[1:]:
                node = insert(key)
                if self.height < node.height:
                    self.height = node.height

    
    def get_root(self):
        """Return the root of the BST."""
        return self.root
    
    def is_empty(self):
        """Return True if the BST is empty."""
        if self.root == None:
            return True
    
    def find_max(self):
        """Return the node with the maximum key in the BST."""
        current = self.root
        maximum = 0
        while 1:
            if current.r.child == None:
                return current
            if maximum < current.key:
                maximum = current.key
                current = current.r_child
    
    def find_min(self):
        """Return the node with the minimum key in the BST."""
        current = self.root
        minimum = math.inf
        while 1:
            if current.l.child == None:
                return current
            if current.key < minimum:
                minimum = current.key
                current = current.l_child
    
    def search(self, key):
        """Return the Node object containing the key if the key exists in
           the BST, else return None."""
        # Start searching from the root node.
        current = self.root
        # Check if tree is not empty.
        if current == None:
            return None
        while 1:
            # Return true if the keys match.
            if current.key == key:
                return current
            # If the key is smaller than the key of the evaluated node,
            # compare the key with the left child of the current node.
            elif key < current.key:
                # Return false if the key is not present in the binary tree.
                if current.l_child == None:
                    return None
                current = current.l_child
            # Else compare it with the right child of the current node.
            elif key > current.key:
                if current.r_child == None:
                    return None
                current = current.l_child
    
    def contains(self, key):
        """ Return True if the key exists in the BST, else return False."""
        # Start searching from the root node.
        current = self.root
        # Check if tree is not empty.
        if current == None:
            return False
        while 1:
            # Return true if the keys match.
            if current.key == key:
                return True
            # If the key is smaller than the key of the evaluated node,
            # compare the key with the left child of the current node.
            elif key < current.key:
                # Return false if the key is not present in the binary tree.
                if current.l_child == None:
                    return False
                current = current.l_child
            # Else compare it with the right child of the current node.
            elif key > current.key:
                if current.r_child == None:
                    return False
                current = current.l_child
    
    def insert(self, key, value=None):
        """Create a new node for this key and value, and insert it into the BST.
           
           Return the new inserted node, or None if the key and value could not
           be inserted."""
        node = Node(key, value)
        node.key = key
        node.value = value
        node.l_child = None
        node.r_child = None
        # If the BST is empty initialize by assigning the node to the root of
        # the tree.
        height = 0
        parent = None
        if is_empty():
            node.height = height
            node.parent = parent
            self.root = node
            list_of_all_nodes.append(node)
            return node
        else:
            current = self.root
            while 1:
                # If the key is smaller than the key of the evaluated node 
                # and there does not exist a left child, make the node to 
                # be inserted the left child of the evaluated node.
                if key < current.key:
                    height += 1
                    if current.l_child == None:
                        node.parent = parent
                        node.height = height
                        current.l_child = node
                        list_of_all_nodes.append(node)
                        return node 
                    # Else evaluate the left child node.
                    else:
                        parent = current
                        current = current.l_child      
                elif key > current.key:
                    height += 1
                    if current.r_child == None:
                        node.parent = parent
                        node.height = height
                        current.r_child = node
                        list_of_all_nodes.append(node)
                        return node
                    else:
                        parent = current
                        current = current.r_child
                # If the key is already present in the BST return None.        
                else:
                    return None

    
    def delete(self, key):
        """Remove the Node object containing the key if the key exists in
           the BST and return the removed node, else return None.
           
           The returned node is the actual Node object that got removed
           from the BST, and so might be successor of the removed key."""
        node = search(self, key)
        if node == None:
            return None
        else:


    def in_order_traversal(self, l=[]):
        """Return a list of the Nodes in the tree in sorted order."""
        node = self.l_child
        in_order_traversal(self.l_child)
        l.append(node)
        node = self.r_child
        in_order_traversal(self.r_child)
    
    
    def breadth_first_traversal(self):
        """Return a list of lists, where each inner lists contains the elements
           of one layer in the tree. Layers are filled in breadth-first-order,
           and contain contain all elements linked in the BST, including the
           None elements.
           >> BST([5, 8]).breadth_first_traversal()
           [[Node(5)], [None, Node(8)], [None, None]]"""
        l = []
        height = 0
        if self.root == None:
            return l
        else:
            current = self.root
            l.append([current])
            
            left_child = current.l_child
            right_child = current.r_child
            current = current.l_child
            for height in range(1, self.height + 2):
                mini_list = []
                for node in BST.list_of_all_nodes:
                    if height == node.height:
                        mini_list.append(node)
                l.append(mini_list)
        return l


    def breadth_first_traversal(self):
        """Return a list of lists, where each inner lists contains the elements
           of one layer in the tree. Layers are filled in breadth-first-order,
           and contain contain all elements linked in the BST, including the
           None elements.
           >> BST([5, 8]).breadth_first_traversal()
           [[Node(5)], [None, Node(8)], [None, None]]"""
        l = []
        height = 0
        if self.root == None:
            return l
        else:
            current = self.root
            l.append([current])
            for height in range(1, self.height + 2):
                mini_list = []
                for node in BST.list_of_all_nodes:
                    if height == node.height:
                        mini_list.append(node)
                l.append(mini_list)
        return l
    
    def __str__(self):
        """Return a string containing the elements of the tree in breadth-first
           order, with each on a new line, and None elements as `_`, and
           finally a single line containing all the nodes in sorted order.
           >> print(BST([5, 8, 3]))
           5
           3 8
           _ _ _ _
           3 5 8
           """
        pass

