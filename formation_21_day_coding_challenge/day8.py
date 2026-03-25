"""
Given a binary tree, convert this to a doubly linked list in the order of the 
in-order traversal. 
This operation should be done in place, not creating any new data structure. 
You must re-use the node's left pointer as the pointer to the previous node 
in the list and the right pointer should be the next node in the list.

At the end, return a pointer the first node in the list.
 /*
  * You may assume the node class is:
  * class Node {
  *   constructor(value, left = null, right = null) {
  *     this.value = value;
  *     this.left = left;
  *     this.right = right;
  *   }
  * }
  */
function tree2list(root) {
  /* your code here */
}
"""
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def tree2list(root):
    prev = [None]
    head = [None]
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        if prev[0] is None:
            head[0] = root
        else:
            prev[0].right = root
            root.left = prev[0]
        prev[0] = root
        dfs(root.right)
    dfs(root)
    return head[0]

        
