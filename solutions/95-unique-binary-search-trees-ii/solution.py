class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        tree = TreeNode(i)
                        tree.left = left_tree
                        tree.right = right_tree
                        trees.append(tree)
            return trees
        return generate_trees(1, n)