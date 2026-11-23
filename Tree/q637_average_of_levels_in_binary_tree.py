from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        avrg = []
        queue = deque([(root)])

        while queue:
            lvl_size = len(queue)
            lvl_sum = 0

            for c in range(lvl_size):
                node = queue.popleft()
                lvl_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            avrg.append(lvl_sum/lvl_size)

        return avrg

def build_tree(values):
    """Turn a LeetCode-style list like [3, 9, 20, None, None, 15, 7] into TreeNodes."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.averageOfLevels(root))




