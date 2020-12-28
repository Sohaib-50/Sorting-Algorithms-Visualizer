def isPerfect(self):
    if self is None:
        return False
        
    if self.left is None:
        if self.right is None:
            return True
        return False
    if self.right is None:
        return False

    left_height = self.left.height()
    left_nodes = self.left.nodecount
    right_height = self.right.height()
    right_nodes = self.