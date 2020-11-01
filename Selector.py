#  Tufts University COMP 131, Summer 2020
#  Selector.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: A Selector Node is a composite whose children are evaluated in 
#               order (left to right). It fails if all children have failed, 
#               otherwise it succeeds. 
#  Purpose:     Selection Node

from Node import Node 

from Task import Task

class Selector(Node):
    """    
    Selector Constructor
    Purpose:    Initialize the fields of a Selection Compoisite Node
    Arguments:  A boolean status True = Success False = Failed, an int 
                given_priority to be used by a Priority Composite Node.
    Returns:    Nothing
    Effects:    Creates a new Condition Node
    Notes:  
    """    
    def __init__(self, status, given_priority):
        super().__init__(status, given_priority, "Selector Composite")
        self.children = []

    """
    add_child
    Purpose:    Add a node to the end of a Selector Node
    Arguments:  child_node [Node] The node to add
    Returns:    Nothing
    Effects:    self.children [List] 
    Notes:  
    """
    def add_child(self, child_node):
        self.children.append(child_node)

    """    
    run
    Purpose:      Runs the Selector Node when it is reached in the Behavior Tree
    Arguments:    Nothing (Self Sufficient)
    Returns:      A Boolean 
    Effects:      The result impacts the path in the decision tree
    Notes:        Try all children until one succeeds 
    """
    def run(self): 
        # print("Running Selector...")
        for child in self.children:
            child.run()
            if (child.status == "Succeeded"):
                self.status = "Succeeded"
                return "Succeeded"
        # print("All Selector Children Failed")
        self.status = "Failed"
        return "Failed"


