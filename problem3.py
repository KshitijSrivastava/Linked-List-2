

## Problem3 (https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1)


class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        
        #define previous pointer
        prev = None
        #define temporary pointer
        temp = curr_node
        
        #till the second last node
        while temp.next:
            #copy the next node's data to the current node
            temp.data = temp.next.data
            # store the current node in prev
            prev = temp
            #go to the next node in LL
            temp = temp.next
        #point prev's next ot None
        prev.next = None
        #delete the temp that is the last node of LL
        del temp