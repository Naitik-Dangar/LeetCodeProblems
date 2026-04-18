import util

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
    
def ListToNode(l1: list) -> ListNode:
    head = ListNode()
    tempNode = head
    for i in l1:
        tempNode.next = ListNode()
        tempNode = tempNode.next 
        tempNode.val = i
    return head.next

def NodeToList(l1: ListNode) -> list:
    toReturn = []
    while l1:
        toReturn.append(l1.val)
        l1 = l1.next
    return toReturn



def testCase(l1, l2):
    print("Input:\nl1 = ")
    print(l1)
    print("l2 = ")
    print(l2)
    l1Node = ListToNode(l1)
    l2Node = ListToNode(l2)
    testSol = Solution()
    outputNode = testSol.addTwoNumbers(l1Node, l2Node)
    outputList = NodeToList(outputNode)
    print("Output: ")
    print(outputList)

util.printCaseHeader(1)
testCase([2,4,3], [5,6,4])
util.printCaseHeader(2)
testCase([0], [0])
util.printCaseHeader(3)
testCase([9,9,9,9,9,9,9], [9,9,9,9])
