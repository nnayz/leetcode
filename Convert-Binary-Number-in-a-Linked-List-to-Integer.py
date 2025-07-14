# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value_to_add = 1
        bin_str = ""
        decimal_repr = 0
        while(head):
            bin_str = str(head.val) + bin_str
            head = head.next

        print(bin_str)
        
        for ch in bin_str:
            if ch == '1':
                decimal_repr += value_to_add
            value_to_add += value_to_add

        return decimal_repr