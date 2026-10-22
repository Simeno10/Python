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

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if len(self.out_stack) > 0:
            return self.out_stack[-1]
        else: 
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]
        

    def empty(self) -> bool:
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            return True
        else: return False

class Solution3:
    def firstBadVersion(self, n: int) -> int:
        left = 1 
        right = n
        while left < right:
            mid = (left + right) // 2    
            if isBadVersion(mid) is True:
                right = mid
            else:
                left = mid + 1
        return left
        
class Solution4:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        dict1 = {}
        for char in magazine:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1
        for char in ransomNote:
            if char not in dict1 or dict1[char] < 1:
                return False
            dict1[char] -= 1
        return True
