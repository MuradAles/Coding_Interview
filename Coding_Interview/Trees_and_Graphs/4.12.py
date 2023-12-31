class Solution:
    def hasPathSum(self, root, target) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return target == root.val
        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(
            root.right, target - root.val
        )
