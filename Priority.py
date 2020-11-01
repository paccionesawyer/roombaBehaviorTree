#  Tufts University COMP 131, Summer 2020
#  Priority.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: Children are evaluated in order of priority
#               It fails if all children have failed, otherwise it succeeds.
#  Purpose:     Abstraction of Classes

from Node import Node 
from Task import Task

import operator

class Priority(Node):
   
    """
    Priority Composite Constructor
    Purpose:    Initialize the fields of a Priority Node
    Arguments:  Status, a boolean value True = Success False = Failed, 
                An int given_priority to be used by a Priority Composite.
    Returns:    Nothing
    Effects:    Creates a new Priority Composite Node, and initializes
                its children.
    Notes:      
    """
    def __init__(self, status, given_priority):
        super().__init__(status, given_priority, "Priority Composite")
        self.children = list()

    """
    add_child
    Purpose:    Add a node to the end of a Sequence Node
    Arguments:  child_node [Node] The node to add
    Returns:    Nothing
    Effects:    self.children [List] 
    Notes:  
    """
    def add_child(self, child_node):
        self.children.append(child_node)
        self.children.sort(key = operator.attrgetter('priority'))
    
    """
    run
    Purpose:    Runs the Priority Node when it is reached in the Behavior 
                Tree.
    Arguments:  Nothing (Self Sufficient)
    Returns:    A Boolean
    Effects:    The result impacts the path in the decision tree
    Notes: 
    """       
    def run(self):
        # print("Running Priority Node")
        self.children.sort(key = operator.attrgetter('priority'))
        
        for child in self.children:
            child.run()
            if (child.status == "Succeeded"):
                self.status = "Succeeded"
                return "Succeeded"
        self.status = "Failed"
        return "Failed"
