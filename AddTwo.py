# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = ""
        num2 = ""
        
        # Traverse l1
        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next
            
        # Traverse l2
        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next

        # Reverse, add, and reverse back
        total = int(num1[::-1]) + int(num2[::-1])
        res_str = str(total)[::-1]

        l3 = ListNode()
        currentNode = l3
        for i in range(len(res_str)):
            currentNode.next = ListNode()
            currentNode = currentNode.next
            currentNode.val = int(res_str[i])

        return l3.next

