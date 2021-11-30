def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not (root.right or root.left)  and root.val == targetSum:
        return True
    targetSum -= root.val
    return self.hasPathSum(root.right,targetSum) or self.hasPathSum(root.left, targetSum)