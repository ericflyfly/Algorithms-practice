""""if not result" is important to save time.
Intuition

Compare height of left and right subtree, if the difference more than 1 set it to be false, otherwise keep checking.
Use return value to maintain the height of the subtree.
Use "global" variable to store the result.
"""


class Solution:

	def isBalanced(self, root: TreeNode) -> bool:
        result = True

        def isBalancedHelper(node):
            nonlocal result
            if not result or node is None:
                return 0
            leftLength = isBalancedHelper(node.left)
            rightLength = isBalancedHelper(node.right)
            if (abs(leftLength - rightLength) > 1):
                result = False
                return 0
            return max(leftLength, rightLength) + 1
            
    isBalancedHelper(root)
    return result

#Any idea other way or modification to improve space complexity?

