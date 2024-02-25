# დავალება 1.

# ლექციაზე განხილულ კოდებს, დააწერეთ კომენტარები თუ რა დროს რა ხდება




# This class represents a single node in a linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# This class represents a linked list data structure.
class LinkedList:
    def __init__(self):
        self.head = None


    # This method adds a new node to the list
    def append(self, data):
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return
        
        # To find the last node in the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        # append the new node to the end of the list
        last_node.next = new_node



    # This method allows you to insert data at a specific index within the list
    def insert(self, index, data):
        new_node = Node(data)

        # If index is 0, insert the new node at the beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # It iterates through the list to find the node at the given index
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index -1:
            current_node = current_node.next
            current_index += 1

        # Insert the new node at the specified index
        new_node.next = current_node.next
        current_node.next = new_node



    # This method is used to delete a node from the list
    def remove(self, index):
        # If index is 0, remove the head node
        if index == 0:
            self.head = self.head.next
            return

        # It iterates through the list to find the node before the one to be removed
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        # If the node to be removed exists, remove it by updating pointers
        if current_node.next:
            current_node.next = current_node.next.next


    # This method displays information about the list
    def display_info(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


# Create a new LinkedList object
linked_list = LinkedList()

linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.display_info()
linked_list.insert(11, 1)
linked_list.insert(15, 2)
linked_list.display_info()
linked_list.remove(2)
linked_list.display_info()





# ////////////////////////////////////////////////////////////
# /////////////////////////STACK//////////////////////////////////
# ////////////////////////////////////////////////////////////



# This class represents a single node in a Stack.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# This class represents a stack data structure
class Stack:
    def __init__(self):
        self.top_node = None
        self.length = 0


    # This method returns if stack is empty or not
    def empty(self):
        return self.length == 0
    

    # It returns a size of the stack
    def size(self):
        return self.length
    
    # This method returns the top item of the stack
    def top(self):
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("Stack is empty!")


    # This method adds a new item at the stack
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1


    # This method removes the last item from the stack
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack is empty!")

        

# Create a new Stack object
stack = Stack()

stack.push(3)
stack.push(10)
stack.push(12)
stack.push(15)
print(stack.top())
print(stack.size())
print(stack.pop())
print(stack.top())
print(stack.size())
