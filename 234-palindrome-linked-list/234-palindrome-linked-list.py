# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # count length
        ptr = head
        l = 1
        while ptr.next:
            l += 1
            ptr = ptr.next
        
        m1 = l // 2
        m2 = l - m1
        
        ptr = head
        for i in range(m2 - 1):
            ptr = ptr.next
            
        # reverse list after middle
        mid = ptr
        
        cur = ptr.next
        prev = None
        nxt = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        mid.next = prev
            
        # check palindrome
        palindrome = True
        
        a = head
        b = mid.next
        for i in range(m1):
            palindrome = palindrome and (a.val == b.val)
            a = a.next
            b = b.next
            
        return palindrome