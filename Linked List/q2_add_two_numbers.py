# Definition for singly list linked list
from enum import nonmember
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # New digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # Update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode(2)
    dumm1 = l1
    l1.next = ListNode(4)
    l1 = l1.next
    l1.next = ListNode(3)

    l2 = ListNode(5)
    dumm2 = l2
    l2.next = ListNode(6)
    l2 = l2.next
    l2.next = ListNode(4)


    # Replace with sample inputs from the problem description
    result = sol.addTwoNumbers(dumm1, dumm2)
    while result:
        print(f"Result: {result.val}")
        result = result.next






