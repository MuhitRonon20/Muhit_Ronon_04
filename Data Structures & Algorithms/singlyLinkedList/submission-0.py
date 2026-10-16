class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        # Dummy head node to simplify head operations
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, i: int) -> int:
        curr = self.head.next
        index = 0
        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            index += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, i: int) -> bool:
        curr = self.head
        index = 0
        while curr and index < i:
            curr = curr.next
            index += 1
        
        if not curr or not curr.next:
            return False
        
        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        return True

    def getValues(self) -> list[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res