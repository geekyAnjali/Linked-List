
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "-> ", end=' ')
            temp = temp.next
        print("END")
        
    
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.insertAtFirst(data)
        elif self.head.next==None:
            self.tail = new_node
            self.head.next =self.tail
            self.tail.prev = self.head
            self.size += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            
        
    def insertAtFirst(self,data):
        new_node = Node(data)
        if self.head is not None:
     
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
            
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            
    def insertAtIndex(self,data,index):
        temp = self.head
        
        if index==1:
            self.insertAtFirst(data)
        elif index<=self.size and index>1:
            for i in range(index-1):
                temp = temp.next
                print(temp.data)
            new_node = Node(data)
        
            
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev.next = new_node
            temp.prev = new_node
        elif index== self.size+1:
            self.insert(data)
        else:
            print("error")
     
    def delete(self):
        if self.size>1:
           self.tail = self.tail.prev  
           self.tail.next = None
           self.size -= 1  
        elif self.size==1:
            self.head = None
            self.size -= 1 
        else:
            print("empty list")
                
    def deleteAtFirst(self):
        if self.head is not None and self.size>1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        if self.size==1:
            self.head = None
    
    
    def deleteAtIndex(self,index):
        temp = self.head
        if self.size >=1:
            if index <self.size and index>1:
                for i in range(index-1):
                    temp = temp.next
                
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.size -= 1
            elif index==1:
                self.deleteAtFirst()
                self.size -= 1
            elif index== self.size:
                self.delete()
                self.size -= 1
            else:
                print("Index not found")
        
            
            
        
li = LinkedList()

li.insertAtFirst(12)
# li.insertAtFirst(14)
# li.insertAtFirst(13)
li.insert(19)
li.insert(18)
li.insert(16)
li.insertAtIndex(90,1)
li.deleteAtIndex(6)
# li.delete() 
# li.deleteAtFirst()   
# li.deleteAtFirst()   
# li.deleteAtFirst()   
# li.deleteAtFirst()   
# # li.delete()    
# li.delete()    
# li.delete()    
# li.delete()    
# li.delete()    
   
# print(li.head.data, li.tail.data,li.tail.next,li.head.prev)
# print(li.tail.data)
# print(li.head.data)
# print(li.head.next.data)
li.display()
