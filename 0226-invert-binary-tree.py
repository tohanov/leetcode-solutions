# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        stack = [root]

        while len(stack) != 0:
            subtree_root = stack.pop()
            subtree_root.left, subtree_root.right = (
                subtree_root.right,
                subtree_root.left,
            )

            if subtree_root.left is not None:
                stack.append(subtree_root.left)
            if subtree_root.right is not None:
                stack.append(subtree_root.right)

        return root


# Time complexity: O(nodes count)
# Space complexity: O(nodes count)
