#  Tufts University COMP 131, Summer 2020
#  Decorator.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: Decorator Node of Behavior Tree, a decorate alters the basic 
#               behavior of the tree-node it is associated with. It's result 
#               possibilities are "Succeeded", "Failed" or "Running". A 
#               decorator can affect any of the other nodes.
#  Purpose:     Abstraction of 

from Node import Node

class Timer(Node):
    """
    Timer Decoractor Constructor
    Purpose:    executes the attached node for a specific amount of
                time
    Arguments:  start_status (String), "Succeeded", "Failed", or "Running" 
                given_priority (int), to be used by a Priority Composite.
                child (Node), the node the decorator is modifying
                time_cycle (int), the amount of time the timer is set to
    Returns:    Nothing
    Effects:    Creates a new Node, and initializes
    Notes:  
    """
    def __init__(self, status, given_priority, child, time_cycle):
        super().__init__(status, given_priority, 
                        "Timer Decorator " + str(time_cycle))
        self.children.append(child)
        self.max        = time_cycle
        self.seconds    = 0

    """
    run
    Purpose:    Runs the Decorator Node when it is reached in the Behavior Tree
    Arguments:  Nothing (Self Sufficient)
    Returns:    A Boolean 
    Effects:    The result impacts the path in the decision tree
    Notes:      Execute all the children sequentially, 
                succeeding if all succeed.
    """
    def run(self, cycle_number):
        if(self.status != "Running"):
            self.start = cycle_number
            self.children[0].run()
            return self.status
        
        if(self.status == "Running"):
            if ((cycle_number - self.start) < self.max):
                self.children[0].run()
                return self.status
            else: 
                if ((cycle_number - self.start) == self.max):
                    self.status = "Succeeded"
                    return self.status
        
        self.status = "Running"
        self.start  = cycle_number
    
        
class Negate(Node):
    """
    Timer Decoractor Constructor
    Purpose:    A Negate decorator reverses the status of the child node.
    Arguments:  start_status (bool), True = Success False = Failed, 
                given_priority (int), to be used by a Priority Composite.
    Returns:    Nothing
    Effects:    Creates a new Node, and initializes
    Notes:  
    """
    def __init__(self, status, given_priority, child):
        super().__init__(status, given_priority, "Negation Decorator")
        self.children.append(child)

    def run(self):
        self.children[0].run()
        # print("Negating", self.children[0].name)
        
        if (self.children[0].status == "Succeeded"):
            self.status = "Failed"
            return "Failed"
        else:
            self.status = "Succeeded"
            return "Succeeded"

class UntilFail(Node):
    """
    Timer Decoractor Constructor
    Purpose:    An Until decorator returns ACTIVE while the child returns      
                SUCCESS. 
    Arguments:  start_status (bool), True = Success False = Failed, 
                given_priority (int), to be used by a Priority Composite.
    Returns:    Nothing
    Effects:    Creates a new Node, and initializes
    Notes:  
    """
    def __init__(self, status, given_priority, child):
        super().__init__(status, given_priority, "Until Fail Decorator")
        self.children.append(child)

    def run(self):
        self.children[0].run()
        if self.children[0].status == "Succeeded":
            self.status == "Running"
        else:
            return "Succeeded"