#  Tufts University COMP 131, Summer 2020
#  Sequence.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: A Sequence Node is a Composite that aggregates tasks
#               Children are evaluated in order (left to right). It fails
#               as soon as one of the children fails, otherwise it succeeds
#  Purpose:     Abstraction of Classes

from Node import Node 

from Task import Task

class Sequence(Node):
    """
    Sequence Composite Constructor
    Purpose:    Initialize the fields of a Sequence Node
    Arguments:  Status, a boolean value True = Success False = Failed, 
                An int given_priority to be used by a Priority Composite.
    Returns:    Nothing
    Effects:    Creates a new Sequence Composite Node, and initializes
                its children.
    Notes:  
    """
    def __init__(self, status, given_priority):
        super().__init__(status, given_priority, "Sequence Composite")
        self.children = []
    
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

    """
    run
    Purpose:    Runs the Sequence Node when it is reached in the Behavior Tree
    Arguments:  Nothing (Self Sufficient)
    Returns:    A Boolean 
    Effects:    The result impacts the path in the decision tree
    Notes:      Execute all the children sequentially, 
                succeeding if all succeed.
    """
    def run(self):
        # print("Running Sequence Node")
        for child in self.children:
            child.run()
            if (child.status == "Failed"):
                self.status = "Failed"
                return "Failed"
        self.status = "Succeeded"
        return "Succeeded"