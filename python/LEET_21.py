# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, list1, list2) :
        list2.next = list1.next
        list1.next = list2


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None : return None 
        elif list1 is None : return list2
        elif list2 is None : return list1

        if list1.val < list2.val : 
            ans = list1
            list1 = list1.next
        else : 
            ans = list2
            list2 = list2.next

        tmp = ans
        while list1 and list2 :
            if list1.val < list2.val :
                tmp.next = list1
                list1 = list1.next
            else :
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        if list1 : tmp.next = list1
        else : tmp.next = list2

        return ans