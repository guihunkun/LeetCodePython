# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if headA==None or headB==None:
        #     return None
        # pa=headA
        # pb=headB
        # while pa!=None:
        #     while pb!=None:
        #         if pa==pb:
        #             return pa
        #         pb=pb.next
        #     pa=pa.next
        #     pb=headB
        # return None
        
        
        if headA==None or headB==None:
            return None
        pa=headA
        pb=headB
        count=0
        while pa!=None and pb!=None:
            if count>2:
                break
            if pa==pb:
                return pa
            if pa.next==None or pb.next==None:
                count+=1
            if pa.next==None:
                pa=headB
            else:
                pa=pa.next
            if pb.next==None:
                pb=headA
            else:
                pb=pb.next
        return None
