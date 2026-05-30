
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.val})"
    
    def as_list(self):
        result = [self.val]
        q = deque([self])
        while q:
            node = q.popleft()
            if not node:
                continue
            
            result.extend([
                None if not node.left else node.left.val,
                None if not node.right else node.right.val])
            q.extend([node.left, node.right])
        
        for i in range(len(result)-1, -1, -1):
            if result[i] is not None:
                break
        return result[:i+1]


# Create tree
def create_tree(values):
    if not values:
        return None
        
    nodes = [TreeNode(v) if v is not None else None for v in values]
    childrens = deque(nodes[1:])

    for n in nodes:
        if n is None:
            continue
        
        if childrens:
            n.left = childrens.popleft()
        if childrens:
            n.right = childrens.popleft()
    return nodes


if __name__ == "__main__":
    # Inputs
    inputs =[
        [3,9,20,None, None,15,7],
        [1,None,2],
        [1],
    ]
    for values in inputs:
        nodes = create_tree(values)
        print([str(n) for n in nodes])
        print(nodes[0].as_list())