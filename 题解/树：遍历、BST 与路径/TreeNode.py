class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __repr__(self) -> str:
        
        if not self:
            return '[]'
        
        result =[]
        
        queue=[self]
        
        while queue:
            node=queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        
        while result and result[-1]=='null':
            result.pop()
        
        return f'{result}'

def convert(vals)->TreeNode:
    root=TreeNode(vals.pop(0))
    queue=[root]
    
    while vals and queue:
        node=queue.pop(0)
        
        if vals[0] is not None:
            node.left=TreeNode(vals.pop(0))
            queue.append(node.left)
        else:
            vals.pop(0)
            
        if vals and vals[0] is not None:
            node.right=TreeNode(vals.pop(0))
            queue.append(node.right)
        elif vals:
            vals.pop(0)
            
    return root