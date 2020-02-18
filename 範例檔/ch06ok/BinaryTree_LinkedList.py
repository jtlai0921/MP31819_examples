class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None

def create_tree(root,val):  #建立二元樹函數
    newnode=tree()
    newnode.data=val
    newnode.left=None
    newnode.right=None
    if root==None:
        root=newnode
        return root
    else:
        current=root
        while current!=None:
            backup=current
            if current.data > val:
                current=current.left
            else:
                current=current.right
        if backup.data >val:
            backup.left=newnode
        else:
            backup.right=newnode
    return root

data=[5,6,24,8,12,3,17,1,9]
ptr=None
root=None
for i in range(9):
    ptr=create_tree(ptr,data[i]) #建立二元樹
print('===以鏈結串列方式建立二元樹,成功===')
