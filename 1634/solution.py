class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = PolyNode(0, 0)
        cur = dummy
        while poly1 or poly2:
            if poly1 and (not poly2 or poly1.power > poly2.power):
                cur.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            elif poly2 and (not poly1 or poly2.power > poly1.power):
                cur.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            else:
                coefficient = poly1.coefficient + poly2.coefficient
                power = poly1.power
                cur.next = PolyNode(coefficient, power)
                poly1 = poly1.next
                poly2 = poly2.next
            cur = cur.next
        return dummy.next