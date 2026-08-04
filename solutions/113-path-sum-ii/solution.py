class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, path_sum):
            if not node:
                return
            path.append(node.val)
            path_sum += node.val
            if not node.left and not node.right and path_sum == targetSum:
                result.append(path[:])
            dfs(node.left, path, path_sum)
            dfs(node.right, path, path_sum)
            path.pop()
        result = []
        dfs(root, [], 0)
        return result