class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = TreeNode(data)
        
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head

        while True:
            if data > cur.data:
                if not cur.right:
                    cur.right = new_node
                    return
                cur = cur.right
            
            elif data < cur.data:
                if not cur.left:
                    cur.left = new_node
                    return
                cur = cur.left
            
            else:
                raise ValueError("Value already in the tree")


    def pre_order(self, root=None):
        if not root:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root=None):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)
        

    def in_order(self, root=None):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=" ")
        self.in_order(root.right)
        

    def delete_node(self, root=None, data=None):
        if not root or not data:
            return
        
        if root.data == data:
            if not root.left and not root.right: return None
            if not root.left and root.right: return root.right
            if root.left and not root.left: return root.left

            pnt = root.right
            while pnt.left: pnt = pnt.left
            root.data = pnt.data
            root.right = self.delete_node(root.right, root.data)
            
        elif root.val > data:
            root.left = self.delete_node(root.left, data)
        else:
            root.right = self.delete_node(root.right, data)

        return root 