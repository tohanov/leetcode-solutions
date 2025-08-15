# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        max_path_length = 1

        while len(stack) != 0:
            subroot, path_length = stack.pop()

            has_left_child = subroot.left is not None
            has_right_child = subroot.right is not None

            if has_right_child:
                stack.append((subroot.right, path_length + 1))
            if has_left_child:
                stack.append((subroot.left, path_length + 1))

            if not (has_left_child or has_right_child):
                max_path_length = max(path_length, max_path_length)

        return max_path_length


# Time complexity: O(|tree rooted at original root|)
# Space complexity: O(max path length) = O(|tree rooted at original root|)
