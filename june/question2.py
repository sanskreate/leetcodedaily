'''2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None:
           
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

         
            total = carry + x + y
            carry = total // 10 
            current.next = ListNode(total % 10)  
            current = current.next  

          
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next  


def create_linked_list(numbers):
    dummy_head = ListNode(0)
    current = dummy_head
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy_head.next


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next
print(output)  
