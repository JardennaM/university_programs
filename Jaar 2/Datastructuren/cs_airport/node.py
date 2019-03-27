class Node(object):
    def __init__(self, key, value=None):
        """Store the key and value in the node and set the other attributes."""
        self.key = key
        self.value = value
        self.parent = None
        self.l_child = None
        self.r_child = None
        self.height = None

    def get_key(self):
        """Return the key of this node."""
        return self.key
    
    def get_value(self):
        """Return the value of this node."""
        return self.value
    
    def get_parent(self):
        """Return the parent node of this node."""
        return self.parent
    
    def get_left_child(self):
        """Return the left child node of this node."""
        return self.l_child
    
    def get_right_child(self):
        """Return the right child node of this node."""
        return self.r_child
    
    def get_height(self):
        """Return the height of this node."""
        return self.height
    
    def update_height(self):
        """Update the height based on the height of the left and right nodes."""
        pass
    
    #
    # You can add any additional node functions you might need here
    #
    
    def __eq__(self, other):
        """Returns True if the node key is equal to other, which can be
           another node or a number."""
        if isinstance(other, int):
            if self.key == other:
                return True
        elif self.key == other.key:
            return True
        return False
    
    def __neq__(self, other):
        """Returns True if the node key is not equal to other, which can be
           another node or a number."""
        if isinstance(other, int):
            if self.key != other:
                return True
        elif self.key != other.key:
            return True
        return False
    
    def __lt__(self, other):
        """Returns True if the node key is less than other, which can be
           another node or a number."""
        if isinstance(other, int):
            if self.key < other:
                return True
        elif self.key < other.key:
            return True
        return False
    
    def __le__(self, other):
        """Returns True if the node key is less than or equal to other, which
           can be another node or a number."""
        if isinstance(other, int):
            if self.key <= other:
                return True
        elif self.key <= other.key:
            return True
        return False
    
    def __gt__(self, other):
        """Returns True if the node key is greater than other, which can be
           another node or a number."""
        if isinstance(other, int):
            if self.key > other:
                return True
        elif self.key > other.key:
            return True
        return False
    
    def __ge__(self, other):
        """Returns True if the node key is greater than or equal to other,
           which can be another node or a number."""
        if isinstance(other, int):
            if self.key >= other:
                return True
        elif self.key >= other.key:
            return True
        return False
    
    def __str__(self):
        """Returns the string representation of the node in format: 'key/value'.
           If no value is stored, the representation is just: 'key'."""
        if self.value is None:
            return f"{self.key}"
        else:
            return f"{self.key}/{self.value}"

