# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        ptr = head
        l.append(ptr.val)
        
        while ptr.next:
            ptr = ptr.next
            l.append(ptr.val)
            
        palindrome = True
        for i in range(len(l)):
            palindrome = palindrome and (l[i] == l[len(l)-i-1])
            
        return palindrome