# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        merged_list = ListNode()

        merged_head = merged_list

        list1_traverse = list1
        list2_traverse = list2



        while ((list1_traverse is not None) and 
               ((list2_traverse) is not None)):
            
            if list1_traverse.val > list2_traverse.val:
                merged_list.next = list2_traverse
                list2_traverse = list2_traverse.next
            else:
                merged_list.next = list1_traverse
                list1_traverse = list1_traverse.next
            
            merged_list = merged_list.next

        merged_list.next = list1_traverse if list1_traverse else list2_traverse
        
        return merged_head.head # this fixes the dummy value i.e. 0 which gets created during initilization