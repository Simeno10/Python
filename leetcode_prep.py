class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        if self.isBalanced(root.left) == True and self.isBalanced(root.right) == True and abs(height(root.left) - height(root.right)) <= 1:
            return True
        else:
            return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        current = head
        while current is not None:
            if current in sett:
                return True
            sett.add(current)
            current = current.next
        return False
