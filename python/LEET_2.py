# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        e = 10
        i = 0

        num_l1 = 0
        while l1 :
            num_l1 += e**i * l1.val
            i += 1
            l1 = l1.next
            

        num_l2 = 0
        i = 0
        while l2 :
            num_l2 += e**i * l2.val
            i += 1
            l2 = l2.next

        print(num_l1, num_l2)

        total = num_l1 + num_l2

        ans = ListNode(total % 10)
        tmp = ans
        
        for i in range(len(str(total))-2, -1, -1) :
            tmp.next = ListNode(int(str(total)[i]))
            tmp = tmp.next

        return ans
            

        