class Node:
    def __init__(self, value, next= None, previous = None):
        self.value = value
        self.nextNode = next
        self.previousNode = previous        #ADD TO SET VALUE TO "PREVIOUS" NODE


    def get_next_node(self):
        return self.next_node
    def get_prev_node(self):                #GETTING "PREVIOUS" NODE
        return self.prviousNode 
        
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value
        
    def set_next_node(self, node):
        self.next_node = node
    def set_prev_node(self, previous):       #SETTING VALUE TO "PREVIOUS" NODE
        self.prviousNode = previous
        
    def __repr__(self):
        return f'<Node: {self.value}>'

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        
    def add(self, number):
        newNode = Node(number, self.root)       # create the new Node
        if self.root:                           #IF THERE IS A ROOT NODE
            self.root.set_prev_node(newNode)    #IF THERE IS A NODE IN THE LINKEDLIST, ADD POINTER TO "PREVIOUS NODE"
        self.root = newNode                     # place it at the very beginning of our LinkedList
        self.size += 1                          # increment the size attribute by +1
        
    def remove(self, number):
        # create a starting point with which to create a point of reference to iterate over all
        # our list items
        current_node = self.root
        
        # create a reference to shift the previous node's next_node attribute to the node that came AFTER
        # the node we just removed
        #prev_node = None
        
        while current_node:
            if current_node.get_value() == number:
                next =current_node.get_next_node()
                previous =current_node.get_prev_node()
                if next:                                    #IF NEXT NODE EXISTS
                    next.set_prev_node(previous)            #SET ITS "PREVIOUS"NODE WITH THE NODE PREVIOUS TO CURRENT
                if previous:                                #IF PREVIOUS NODE EXISTS
                    previous.set_next_node(next)            #SET ITS "NEXT" NODE WITH THE NODE NEXT TO CURRENT
                else:
                    self.root = current_node
                self.size = self.size -1

                if prev_node:
                    prev_node.set_next_node(current_node.get_next_node())
                else:
                    self.root = current_node.get_next_node()
                self.size -= 1
                return 'Node removed'
            else:
                prev_node = current_node
                current_node = current_node.get_next_node()
        return 'Node not found'
    
    def find(self, number):
        current_node = self.root
        
        prev_node = None
        
        while current_node:
            if current_node.get_value() == number:
                return True
            else:
                current_node = current_node.get_next_node()
        return False
    
    def get_root(self):
        return self.root
    
    def get_size(self):
        return self.size