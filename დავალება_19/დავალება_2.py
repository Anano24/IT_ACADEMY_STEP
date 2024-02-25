# დავალება 2.

# დაწერეთ value გადაწოდების შედეგად ამოშლის ლოგიკა დაკავშირებულ სიებში





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



    # To delete a node by its value
    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return
        
        # It iterates through the list to find the node with the specified value
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next



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
linked_list.append(33)
linked_list.display_info()
linked_list.remove_by_value(10)
linked_list.display_info()


