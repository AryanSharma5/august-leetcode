import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        mapper = collections.defaultdict(list)
        while queue:
            size = len(queue)
            temp = collections.defaultdict(list)
            for i in range(size):
                cur_node, hd = queue.pop(0)
                temp[hd].append(cur_node.val)
                if cur_node.left:
                    queue.append((cur_node.left, hd-1))
                if cur_node.right:
                    queue.append((cur_node.right, hd+1))
            for k, arr in temp.items():
                mapper[k].extend(sorted(arr))
        return [mapper[i] for i in sorted(mapper)]