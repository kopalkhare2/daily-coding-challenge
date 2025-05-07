class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
    
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    
        first, second = head, prev
        result = True
        while second:
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next

        prev_restored = None
        while prev:
            nxt = prev.next
            prev.next = prev_restored
            prev_restored = prev
            prev = nxt
        
        return result
