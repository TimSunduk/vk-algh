#check if list is cycled



def hasCycle(head):
    if head == null or head.next == null:
        return false
    slow = head
    fast = head.next

    while slow != fast:
        if fast == null or fast.next == null:
            return false
        slow = slow.next
        fast = fast.next.next

    return true


#reversedLinkedList
def revLinkList(head):
    prev = null
    current = head
    
    while current != null:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    head = prev
    return head

#find middleNode
def middleNode(node):
    slow = fast = node
    while fast != None and fast.next != None :
        slow = slow.next
        fast = fast.next.next

    return slow

# head == node here

def removeElements(node,val):
    dummy = Node  #
    dummy.next = node
    prev = dummy
    cur = node

    while (cur!= None):
        if (cur.val == val):
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    return dummy.next


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

node1=Node(1)
node2=Node(3)
node3=Node(5)
node4=Node(7)
node5=Node(9)
node6=Node(11)


node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=None

def print_list(node):
    while node:
        print(node)
        node = node.next

print_list(node1)
removeElements(node1,7)
print_list(node1)
