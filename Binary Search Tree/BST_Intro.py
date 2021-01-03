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


def inorder(root): # agacın kökünü yolluyoruz
    
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
inorder(r)    
    
result = search(r,80)  # Var olan bir deeger
print(result.val)

result2 = search(r,1233)  # var olmayan bir deger
print(result2) #none donduırur 
    
    
        
    