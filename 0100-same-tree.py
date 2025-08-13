# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]

        while len(stack1) != 0:
            # if not len(stack1) == len(stack2):
            #     return False

            subtree_root1 = stack1.pop()
            subtree_root2 = stack2.pop()

            if (
                subtree_root1 is None
                and subtree_root2 is not None
                or subtree_root1 is not None
                and subtree_root2 is None
            ):

                return False

            if (
                subtree_root1 is not None and subtree_root2 is not None
            ) and subtree_root1.val != subtree_root2.val:

                return False

            if subtree_root1 is not None:
                stack1.append(subtree_root1.left)
                stack1.append(subtree_root1.right)

                stack2.append(subtree_root2.left)
                stack2.append(subtree_root2.right)

        return True
