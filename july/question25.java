/*25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?*/

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        
        List<Integer> list = new ArrayList<>();
        ListNode temp = head;
        while(temp != null) {
            list.add(temp.val);
            temp = temp.next;
        }

        for(int i=0; i<=list.size()-k; i+=k) {
            reverse(i, i+k-1, list);
        }

        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;
        for(int i : list) {
            ListNode node = new ListNode(i);
            curr.next = node;
            curr = curr.next;
        }
        return dummy.next;
        
    }

    static void reverse(int l, int r, List<Integer> list)
    {
        while(l < r){
            int t = list.get(l);
            list.set(l, list.get(r));
            list.set(r, t);
            ++l;
            --r;
        }
    }
}
