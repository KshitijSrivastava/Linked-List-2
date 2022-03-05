
## Problem4  (https://leetcode.com/problems/intersection-of-two-linked-lists/)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_length(self, head):
        """
        For getting the length of the linkedlist
        """
        count = 0
        temp = head
        
        while temp:
            count += 1
            temp = temp.next
            
        return count
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lengthA = self.get_length(headA)    #get the length of the linkedlist A
        lengthB = self.get_length(headB)    #get the length of the linkedlist B
        
        #initilize the temp to point to the head
        tempA = headA
        tempB = headB
        
        # if ll A is longer than ll B then shift the pointer of A
        if lengthA > lengthB:
            diff = lengthA - lengthB
            
            while diff > 0 and tempA:
                tempA = tempA.next
                diff -= 1
        # if ll A is longer than ll B then shift the pointer of B
        elif lengthA < lengthB:
            diff = lengthB - lengthA
            
            while diff > 0 and tempB:
                tempB = tempB.next
                diff -= 1
        #now both the LL heads are of equal distance from None 
        #while bith node exists
        while tempA and tempB:
            #if both the node are equal return it
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
            
        return None