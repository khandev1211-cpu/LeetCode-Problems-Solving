class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                if i < level_size - 1:
                    queue[i].next = queue[i + 1]
                else:
                    queue[i].next = None
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[level_size:]
        return root