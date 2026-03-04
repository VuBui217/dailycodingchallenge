"""
Problem 1: 
Given a linked list, delete the middle node. If the list is even length, 
delete the node at the start of the second half of the list.
/*
  * You may assume the node class is:
  * class LLNode {
  *   constructor(value, next = null) {
  *     this.value = value;
  *     this.next = next;
  *   }
  * }
  */
function deleteMiddleNode(head) {
  /* your code here */
}
"""
"""
Scratch"

dummy -> 1 -> 2 -> 3 -> 4
              s
                           f

dummy -> 1 -> 2 -> 3 -> 4 -> 5
              s
                             f
"""
# Node class
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def print_ll(head):
    curr = head
    output = []
    while curr:
        output.append(str(curr.val))
        curr = curr.next
    print("->".join(output))


def deleteMiddleNode(head):
    dummy = ListNode(-1)
    dummy.next = head

    slow, fast = dummy, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next

    return dummy.next

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))
print_ll(deleteMiddleNode(l1))


