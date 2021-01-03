class Node:
    def __init__(self,val):
        self.right = None
        self.left = None
        self.val = val

def insert(root,node):
    if root is None:
        root = node
    
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)


def inorder(root): 
    
    if root is None:
        return 
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
    
def search(root,key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right,key)
    else:
        return search(root.left,key)
    
    
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current
        
def deleteNode(root, key): 
  
    if root is None: 
        return root  
  
    if key < root.val: 
        root.left = deleteNode(root.left, key) 
   
    elif(key > root.val): 
        root.right = deleteNode(root.right, key) 
    else: 
          
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 

        temp = minValueNode(root.right) 
        root.val = temp.val 
        root.right = deleteNode(root.right , temp.val)  
    return root  




# main ()
    
    
r = Node(100)
insert(r,Node(90))
insert(r,Node(130))
insert(r,Node(85))
insert(r,Node(95))
insert(r,Node(80))
insert(r,Node(87))
insert(r,Node(120))
insert(r,Node(140))

r=deleteNode(r,100) # koku çıkardık
inorder(r)