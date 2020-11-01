#  Tufts University COMP 131, Summer 2020
#  Node.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: Parent Class for all Nodes in the Behavior Tree
#  Purpose:     Abstraction of Classes

class Node:

    """
    Node Constructor
    Purpose:    Initialize the fields of a General Node
    Arguments:  start_Status   [bool]   True = Success False = Failed, 
                given_priority [int]    To be used by a Priority Composite.
                given_name     [string] Name of node, if no name is necessary 
                                        the type of Node is given
    Returns:    Nothing
    Effects:    Creates a new Node, and initializes
    Notes:      
    """
    def __init__(self, start_status, given_priority, given_name):
        self.status     = start_status
        self.priority   = given_priority
        self.children   = []
        self.name       = given_name

    """
    print_subtree
    Purpose:    Prints a tree 
    Arguments:  level [int], The recursive call
    Returns:    Nothing
    Effects:    Prints to the terminal
    Notes:      
    """
    def print_subtree(self, level = 0):
        print ('\t' * level + repr(self.name))
        for child in self.children:
            child.print_subtree(level + 1)
        
