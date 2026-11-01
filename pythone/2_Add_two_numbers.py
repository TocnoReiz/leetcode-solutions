class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        d = ListNode()
        cur = d
        car = 0
        while l1 or l2 or car:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a+b+car
            
            car = total//10
            cur.next = ListNode(total%10)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return d.next