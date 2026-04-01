"""
Given a binary tree, find the height, that is the length of the path from the root to the deepest leaf node.
/*
 * You may assume the node class is:
 * class TreeNode {
 *   constructor(value, left = null, right = null) {
 *     this.value = value;
 *     this.left = left;
 *     this.right = right;
 *   }
 * }
 */
function treeHeight(root) {
  /* your code here */
}
"""
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def treeHeight(root):
    if not root:
        return 0

    # Using bfs
    # from collections import deque
    # q = deque()
    # q.append(root)
    # height = 0
    # while q:
    #     lenq = len(q)
    #     for _ in range(lenq):
    #         curr = q.popleft()
    #         if curr.left:
    #             q.append(curr.left)
    #         if curr.right:
    #             q.append(curr.right)
    #     height += 1
    
    left_height = treeHeight(root.left)
    right_height = treeHeight(root.right)

    return 1 + max(left_height, right_height)