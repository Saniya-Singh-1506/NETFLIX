class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
node1=Node(10)

#create 2nd node + link it from the first1    
node2=Node(20)
node1.next=node2

node3=Node(30)
node2.next=node3
    
current = node1
while current:
    print(current.data , end = " ->")
    current = current.next
print("None")