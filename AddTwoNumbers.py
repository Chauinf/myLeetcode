# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        isHead = True
        carry = False
        now = head  = ListNode(0)
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val
            if carry is True:
                sum += 1
                carry = False
            
            if sum >= 10:
                carry = True
                sum = sum - 10
                
            tmp = ListNode(sum)

            if isHead is True:
                head.next = tmp
                isHead = False
                
            now.next = tmp
            now = now.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            if carry is True:
                l1.val += 1
                carry = False
            if l1.val >= 10:
                carry = True
                l1.val -= 10
            tmp = ListNode(l1.val)
            now.next = tmp
            now = now.next
            l1 = l1.next
            
        while l2 is not None:
            if carry is True:
                l2.val += 1
                carry = False
            if l2.val >= 10:
                carry = True
                l2.val -= 10
            tmp = ListNode(l2.val)
            now.next = tmp
            now = now.next
            l2 = l2.next
            
        if carry is True:
            tmp = ListNode(1)
            now.next = tmp
            now = now.next
            
            
            
        return head.next