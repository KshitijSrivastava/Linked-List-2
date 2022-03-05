

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_LL(self, head):
        """ To reverse a linked list"""
        
        prev = None
        temp = head
        
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            
        return prev
    
    def print_LL(self, head):
        """ To print a linked list"""
        temp = head
        
        arr = []
        while temp:
            arr.append( str(temp.val) )
            temp = temp.next
            
        print("->".join(arr) )
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        prev = None
        slow = head
        fast = head
        
        #use slow and fast pointer to find the mid point
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        head_half = slow.next
        slow.next = None
        new_head = None
        
        tempA = head
        tempB = head_half
        #reverse the second half of linked list
        tempB = self.reverse_LL(tempB)
        
        #self.print_LL(tempA)
        #self.print_LL(tempB)
        
        #while second half is not empty
        while tempB:
            #keep track of the next pointer
            nxtA = tempA.next
            nxtB = tempB.next
            
            #point the pointers to each other
            tempA.next = tempB
            tempB.next = nxtA
            
            #advance the pointer
            tempA = nxtA
            tempB = nxtB
            
        return head
        
        