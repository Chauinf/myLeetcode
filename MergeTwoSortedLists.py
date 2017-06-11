# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        isHead = True
        head = ListNode(0)
        now = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp = ListNode(l2.val)
                l2 = l2.next
            
            now.next = tmp
            now = now.next
            
            if isHead is True:
                isHead = False
                head.next = tmp
        
        while l1 is not None:
            tmp = ListNode(l1.val)
            now.next = tmp
            now = now.next
            l1 = l1.next
            if isHead is True:
                isHead = False
                head.next = tmp
        
        while l2 is not None:
            tmp = ListNode(l2.val)
            now.next = tmp
            now = now.next
            l2 = l2.next
            
            if isHead is True:
                isHead = False
                head.next = tmp
            
        return head.next