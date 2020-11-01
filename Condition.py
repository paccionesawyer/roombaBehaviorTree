#  Tufts University COMP 131, Summer 2020
#  Condition.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: Condition Node of Behavior Tree, a condition tests some 
#               property of the system. It's result possibilities are 
#               "Succeeded" or "Failed". A condition is directly found in the 
#               blackboard
#  Purpose:     Abstraction of Classes

from Node import Node 

class Condition(Node):
    """
    Condition Constructor
    Purpose:    Initialize the fields of a Condition Node
    Arguments:  A string given_name to differentiate the node while printing
                a boolean status True = Success False = Failed, an int 
                given_priority to be used by a Priority Composite Node.
                Condition, a function that returns a boolean, to be run 
                whenever the condition Node is called. *args are the 
                arbitrary arguments of the condition functions
    Returns:    Nothing
    Effects:    Creates a new Condition Node
    Notes:  
    """
    def __init__(self, start_status, given_priority, given_name, condition, 
                *args):
        super().__init__(start_status, given_priority, given_name)
        self.name       = given_name
        self.condition  = condition
        self.my_args    = args
    
    """
    run
    Purpose:    Runs the condition Node when it is reached in the Behavior    
                Tree
    Arguments:  Nothing (Self Sufficient)
    Returns:    A Boolean 
    Effects:    The result impacts the path in the decision tree
    Notes: 
    """ 
    def run(self):
        print("Running Condition:", [self.name], "...")
        self.status = self.condition(*self.my_args)
        print("Condition", [self.name], self.status)
        return self.status



