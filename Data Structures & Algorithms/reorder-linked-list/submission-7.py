# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 4 6 8 10 12
        #       s        f

        # 2  4  6
        # 12 10 8

        # 2 12 4 10 6 8


        # 2 4 6 8 10
        #     s   f

        # 2      4
        # head
        # 10     8    6
        # new_h
        # 2 10 4 8 6

        def reverse(h):
            pre = None

            while h is not None:
                next_node = h.next
                h.next = pre
                pre = h
                h = next_node
            return pre

        def merge(h1, h2):
            # list2 : 前半段
            # list1 : reverse过的后半段
            # head1 是list1的头结点
            # head2 是list2的头结点
            # 现在要把list1一个个插到list2中间
            mergedHead = h2
            while h1 is not None:
                next1 = h1.next
                next2 = h2.next

                h2.next = h1 # head2 -> head1
                h1.next = next2 # head1 ->head2next

                h1 = next1
                h2 = next2
            return mergedHead
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        secondHead = s.next

        s.next = None
        secondHead = reverse(secondHead)

        merge(secondHead, head)


