"""
This is a more complex list traversal problem. In this case, each node points to the next in the current list, 
but may also have a sublist. Think of this like an outline. At the top level, there is a list of bullet points. 
Each bullet might have sub-bullets, which themselves might have sub-bullets.

The task is to flatten this into an output array. All of every node's sub bullets must come before the next bullet at that node's level.
/*
  * The node class for this is a simple extension of before:
  * class LLNode {
  *   constructor(value, next = null, sublist = null) {
  *     this.value = value;
  *     this.next = next;      // the next value in the current list
  *     this.sublist = sublist; // another list
  *   }
  * }
  */
function flattenSublist(head) {
  const output = [];

  /* your code here */

  return output;
}
"""
# Python
class LLNode:
    def __init__(self, val, next=None, sublist=None):
        self.val = val
        self.next = next
        self.sublist = sublist


def flattenSublist(head):
    output = []

    # if not head:
    #     return output
    
    # curr = head

    # while curr:
    #     output.append(curr.val)
    #     if curr.sublist:
    #         output.extend(flattenSublist(curr.sublist))
    #     curr = curr.next

    def dfs(node):
        if not node:
            return
        if node.val:
            output.append(node.val)
        dfs(node.sublist)
        dfs(node.next)
    dfs(head)
    return output

# Test 1: No sublist (flat list)
# 1 -> 2 -> 3
head = LLNode(1, LLNode(2, LLNode(3)))
assert flattenSublist(head) == [1, 2, 3]

# Test 2: Single level sublist
# 1 -> 2 -> 3
#      |
#      4 -> 5
node2 = LLNode(2, LLNode(3))
node2.sublist = LLNode(4, LLNode(5))
head = LLNode(1, node2)
assert flattenSublist(head) == [1, 2, 4, 5, 3]

# Test 3: Nested sublist (2 levels deep) — the case your original code missed
# 1 -> 2
#      |
#      3 -> 4
#           |
#           5 -> 6
node4 = LLNode(4)
node4.sublist = LLNode(5, LLNode(6))
node3 = LLNode(3, node4)
node2 = LLNode(2)
node2.sublist = node3
head = LLNode(1, node2)
assert flattenSublist(head) == [1, 2, 3, 4, 5, 6]

# Test 4: Empty list
assert flattenSublist(None) == []

# Test 5: Single node, no sublist
assert flattenSublist(LLNode(42)) == [42]

print("All tests passed!")
