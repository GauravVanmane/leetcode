def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root:
        order , stack = [], [root]
        while stack:
            node = stack.pop()
            order.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return order
    else:
        return []