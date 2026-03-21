class ListNode:
    """A node in the singly linked list"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers represented by linked lists"""
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next


# ==========================================
# Test Code

def build_linked_list(arr):
    """Helper function: Convert a Python list to a linked list"""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(node):
    """Helper function: Print the linked list in a readable format"""
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))


if __name__ == "__main__":
    solution = Solution()

    print("Test Case 1: [2, 4, 3] + [5, 6, 4]")
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result1 = solution.addTwoNumbers(l1, l2)
    print("Output:   ", end="")
    print_linked_list(result1)  # 7 -> 0 -> 8

