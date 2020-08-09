# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        def recurse(root, sum, currPath):
            if not root:
                return
            currPath.append(root.val)
            recurse(root.left, sum, currPath)
            recurse(root.right, sum, currPath)
            currSum = 0
            for i in range(len(currPath) - 1, -1, -1):
                currSum += currPath[i]
                if currSum == sum:
                    self.ans += 1
            currPath.pop()
        recurse(root, sum, [])
        return self.ans