# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LeetCode#515 Problem. You need to find the largest value in each row of a binary tree.

# Use BFS to go through every node in every row and find the largeset number in every row

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.append(root.val)
            row = [root]
            while row:
                maxNum = float("-inf")
                newRow = []
                for node in row:
                    if node.left:
                        newRow.append(node.left)
                        maxNum = max(maxNum, node.left.val)
                    if node.right:
                        newRow.append(node.right)
                        maxNum = max(maxNum, node.right.val)
                row = newRow
                result.append(maxNum)
            result.pop()
        return result