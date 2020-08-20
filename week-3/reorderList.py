# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        def findMid():
            fast = slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse():
            mid, prev = findMid(), None
            curr = mid
            while curr:
                np = curr.next
                curr.next = prev
                prev = curr
                curr = np
            return prev
        if not head:return
        last = reverse()
        start = head
        np = start.next
        while last.next:
            start.next = last
            last = last.next
            start.next.next = np
            start = np
            if start:np = start.next
        return head