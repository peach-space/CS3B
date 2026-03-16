#################################################
# CS03B - Winter 2026
# Assignment 3
# Student Name: Cen Li
# SID: 20713344
#################################################

# Question 1
def findDisappearedNumbers(nums):
    n = len(nums)
    num_set = set(nums)
    return [i for i in range(1, n + 1) if i not in num_set]


# Question 2
def generate(numRows):
    if numRows == 0:
        return []

    triangle = [[1]]

    for i in range(1, numRows):
        prev_row = triangle[-1]
        curr_row = [1]

        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle

# Question 3
def decodeString(s):
    stack = []
    curr_str = ""
    curr_num = 0

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += char

    return curr_str

# Question 4
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA


# test function
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def get_tail(head):
    if not head: return None
    curr = head
    while curr.next:
        curr = curr.next
    return curr


if __name__ == "__main__":
    print("--- Testing Question 1: Disappeared Numbers ---")
    input_arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"Input: {input_arr}")
    print(f"Output: {findDisappearedNumbers(input_arr)}\n")

    print("--- Testing Question 2: Pascal Triangle ---")
    input_num = 5
    print(f"Input: {input_num}")
    print("Output:")
    result = generate(input_num)
    for row in result:
        print(row)
    print()

    print("--- Testing Question 3: Decode String ---")
    test_cases = [
        "3[a]2[bc]",
        "3[a2[c]]",
        "2[abc]3[cd]ef",
        "abc3[cd]xyz"
    ]
    for tc in test_cases:
        print(f"Input: {tc}")
        print(f"Output: {decodeString(tc)}")
    print()

    print("--- Testing Question 4: Intersection of Two Linked Lists ---")
    common = create_linked_list([8, 4, 5])

    headA = create_linked_list([4, 1])
    if headA: get_tail(headA).next = common

    headB = create_linked_list([5, 6, 1])
    if headB: get_tail(headB).next = common

    res = getIntersectionNode(headA, headB)
    print(f"Output: Intersection at node with value = {res.val if res else 'null'}")