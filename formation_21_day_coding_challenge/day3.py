"""
Given a linked list, reverse groups of k nodes. These groups will remain in order themselves. 
For example, if we perform this operation with k=2 on the following list:
1 -> 2 -> 3 -> 4-> 5
The result will be:
2 -> 1 -> 4 -> 3 -> 5
Once again, this should be done in-place, just re-assigning the next pointers in the nodes and returning the new head. 
The head parameter will be a list of some length (possibly zero) and k will be a positive integer.
/*
 * You may assume the node class is:
 * class LLNode {
 *   constructor(value, next = null) {
 *     this.value = value;
 *     this.next = next;
 *   }
 * }
 */
function reverseInGroupsOfK(head, k) {
  /* your code here */
}
"""
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
    
    print('->'.join(output))

def get_next_group(group_start, k):
    curr = group_start
    while k > 0:
        if curr is None:
            return None
        curr = curr.next
        k -= 1
    return curr

def reverse(group_start, next_group):
    # Set prev to next_group so the tail of the reversed segment
    # automatically points to the start of the next group
    prev = next_group
    curr = group_start
    while curr != next_group:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev  # new head of this reversed group

def reverseInGroupOfK(head, k):
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next

    if not head:
        return None

    reverse_count = n // k
    group_start = head
    next_group = None
    new_head = None    # head of the fully modified list
    prev_tail = None   # tail of the previously reversed group

    while reverse_count > 0:
        next_group = get_next_group(group_start, k)
        new_group_head = reverse(group_start, next_group)

        if prev_tail:
            prev_tail.next = new_group_head  # stitch previous tail to current new head
        else:
            new_head = new_group_head        # first iteration: this is the new list head

        prev_tail = group_start  # group_start is now the tail after reversal
        group_start = next_group
        reverse_count -= 1

    return new_head
