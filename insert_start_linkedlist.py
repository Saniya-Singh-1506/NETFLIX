class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
#creating nodes
node1=Node(10)
node2=Node(20)
node3=Node(30)

#linking nodes
node1.next=node2
node2.next=node3

current=node1
while current:
    print(current.data,end="->")
    current=current.next
print(None)