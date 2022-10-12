
class Node():
    '''
    each element in linked list is considered as a Node 
    and it's consist of data and the address of the next Node

    '''
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self,data):
        if self.head==None and self.tail==None:
            self.head = Node(data)
            self.size +=1
        else: 
            item  = Node(data)
            if self.head!=None and self.head.next==None:
                self.head.next = item
                self.tail = item
                self.size +=1
            else:
                self.tail.next = item
                self.tail = item
                self.size +=1
                
            
    
    def insertAtFirst(self,data):
        '''
        insertion of elemnet from the head Node
        '''
        new_node = Node(data)
        new_node.next = self.head
        self.head   = new_node
        self.size += 1
    
    
    def insertAtIndex(self,indx,data):
        '''
        insertion of element at any index
        '''
        if self.size>=1:
            if indx==1:
                self.insertAtFirst(data)
            elif indx==self.size+1:
                self.insert(data)
               
            elif indx<=self.size:
                new_node = Node(data)
                temp = self.head
                for i in range(indx-1):
                    if i == indx-2:
                        prev_node = temp
                    temp = temp.next
                new_node.next = temp
                prev_node.next = new_node
            else:
                print("size of linked list is ->"+ str(self.size))
                
        else:
            print("Index start from 1")
                
                
        
    def deleteAtLast(self):
        'delete the Last element'
        if self.head!=None:
            temp = self.head
            for _ in range(self.size-2):
                temp = temp.next
        
            self.tail = temp
            self.tail.next = None
            self.size -= 1
        else:
            print("The list is blank")
              
    
    def deleteAtfirst(self):
        '''
        delete first element
        '''
        if self.head!=None:
            self.head = self.head.next
            self.size -=1
        else:
           print("The list is blank") 
        
    
    def deleteAtIndext(self,index):
        '''
        delete at any indext
        '''
        if index<=self.size:
            temp = self.head
            for i in range(index):
                if i==index-2:
                    prev_node = temp
                temp = temp.next
                
            prev_node.next = temp
        else:
            print("index out of range")    
    
    def display(self):
        if self.head!=None:
            temp = self.head
            while(temp):
                print(str(temp.data)+"->",end=' ')
                
                temp =temp.next
            print("END")
        else:
            print("Sorry, List is empty.") 

if __name__ == '__main__':
    li = LinkedList()
    print("Do you want to perform operations in linked list : y/n ")
    n = input("\n print y if yes or n if no : ")
    print("id and the  operations' number \n 1. insert \n 2. insertAtFirst \n 3. insertAtLast \n 4. InsertAtIndex \n 5. display \n 6. deleteAtFirst \n 7. deleteLast \n 8. deleteAtIndex")
    
    
    while n=='y':
        
       
        opr = int(input("\n Enter operation id : "))
    
    
        if opr == 1 :
            data = input("Enter a value : ")
            li.insert(data)
        elif opr == 2:
            data = input("Enter a Value")
            li.insertAtFirst(data)
        elif opr==3:
            data = input("Enter a Value")
            li.insert(data)
        elif opr==4:
            data = input("Enter a Value")
            index = input("Enter index number")
            li.insertAtIndex(data)
            
        elif opr==5:
            print("your list is : ")
            li.display()
        elif opr==6:
            li.deleteAtfirst()
            print("First element deleted successfully !")
        elif opr==7:
            li.deleteAtLast()
            print("element delted successfully !")
        
        elif opr==8:
            idx = int(input("Enter the index number"))
            li.deleteAtIndext(idx)
        else:
            print("you have entered wrong id")    
        
        n = input("print y if yes or n if no : ")
        if n=='n':
            break   
    else:
        print("Operation exited")
 
