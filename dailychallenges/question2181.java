/*2181. Merge Nodes in Between Zeros

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
Return the head of the modified linked list.

Example 1:

Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Example 2:

Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4. 

Constraints:

The number of nodes in the list is in the range [3, 2 * 105].
0 <= Node.val <= 1000
There are no two consecutive nodes with Node.val == 0.
The beginning and end of the linked list have Node.val == 0.*/

class Solution {
    public ListNode mergeNodes(ListNode head) {

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int sum = 0;
        
        head = head.next;
        
        while (head != null) {
            if (head.val == 0) {
              
                current.next = new ListNode(sum);
                current = current.next;
                sum = 0;
            } else {
                sum += head.val;
            }
            head = head.next;
        }
        
        return dummy.next;
    }

    public static ListNode createLinkedList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int num : arr) {
            current.next = new ListNode(num);
            current = current.next;
        }
        return dummy.next;
    }
    
    public static int[] linkedListToArray(ListNode head) {
        List<Integer> result = new ArrayList<>();
        while (head != null) {
            result.add(head.val);
            head = head.next;
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
    
    public static void main(String[] args) {
      
        int[] input1 = {0, 3, 1, 0, 4, 5, 2, 0};
        ListNode head1 = createLinkedList(input1);
        Solution solution = new Solution();
        ListNode newHead1 = solution.mergeNodes(head1);
        int[] output1 = linkedListToArray(newHead1);
        System.out.println(Arrays.toString(output1));

        int[] input2 = {0, 1, 0, 3, 0, 2, 2, 0};
        ListNode head2 = createLinkedList(input2);
        ListNode newHead2 = solution.mergeNodes(head2);
        int[] output2 = linkedListToArray(newHead2);
        System.out.println(Arrays.toString(output2)); 
    }
}
