from node import Node


'''
LLstack is a class
this class is a single linked list without a tail it acts as a stack full of immutable nodes
'''
class LLStack:
    
    '''
    intializes the head to ne none and size to be 0
    '''
    def __init__(self) -> None:
        self.__head = None
        self.__size = int(0)
    
    
    '''
    pop acts like a pop funtion from a list but it updates size to be -1 when an element is removed and 
    then prints the element also needs to be a tuple as the data should not be changed
    '''
    def pop(self) -> tuple:
        
        # makes sure that your not trying to pop an empty list and raises an IndexError if you do
        if self.__head == None:
            raise IndexError("pop wont work if there is no head")
        
        # sets data varible to be the same as the top element in a stack
        data = self.__head.data
        
        # makes size -1 as an element is be removed
        self.__size -= 1
        
        # sets new head to be the next element from the top in the stack 
        self.__head = self.__head.next
        return data
    
    '''
    push adds an element to the list and adds a new element/node to the top of the lsit essentially push 
    the rest of the nodes back by one
    '''
    def push(self, data: tuple):
        
        # checks if data being added is a tuple and if its not raises a type error
        if not isinstance(data, tuple):
            raise TypeError('data isnt a tuple')
        
        # sets new node to be the data being pushed in
        new_node = Node(data)
        
        # sets the new nodes next to be the last added elment
        new_node.next = self.__head  
        
        # new head is going to be the new node 
        self.__head = new_node  
        
        # increases size by 1
        self.__size += 1
    
    
    '''
    returns a readable size
    '''
    @property
    def size(self):
        return self.__size
        
    '''
    prints the value of the node and ands an arrow (->) pointing to the next node
    '''
    def __str__(self) -> str:
        
        # sets string to be a string
        string = ''
        
        # curr is the same as the top node of the stack
        curr = self.__head
        
        # makes sure that the top node isnt none and raises typeerror if it is
        if curr == None:
            raise TypeError('curr isnt a value')
        
        # goes on untill next is none and prints the value with an -> to the next node
        while curr.next is not None:
            string += str(curr) + '->'
            curr = curr.next
        string += curr.__str__()
        return string
    