'''1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]
 
Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 10^5'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
           
            nodes = []
            def inorder(node):
                if not node:
                    return
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
            inorder(node)
            return nodes

        def build_balanced_bst(nodes, start, end):
        
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = build_balanced_bst(nodes, start, mid - 1)
            node.right = build_balanced_bst(nodes, mid + 1, end)
            return node

        nodes = inorder_traversal(root)

        return build_balanced_bst(nodes, 0, len(nodes) - 1)

def print_tree(root):
    if not root:
        return "[]"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
   
    while result and result[-1] is None:
        result.pop()
    return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

solution = Solution()
balanced_root = solution.balanceBST(root)
print(print_tree(balanced_root))  
