#  Tufts University COMP 131, Summer 2020
#  Task.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: Task Node of Behavior Tree, a Task alters the state  of the 
#               system. It's result possibilities are "Succeeded", 
#               "Failed", "Running". A task can affect the blackboard,
#               or can be affected by the blackboard.
#  Purpose:     A task alters the state of a program, it can succeed, fail or  
#               continue running

import random

from Node import Node 

class Task(Node):
    
    """
    Task Node Constructor
    Purpose:    Initialize the fields of a Task Node
    Arguments:  given_name, the name of the task (string)
                given_success, the success rate of the task (int)
                start_status, the initial state of the task (bool)
                given_priority, the priority of the node (int) 
    Returns:    Nothing
    Effects:    Creates a new Task Node
    Notes:   
    """
    def __init__(self, start_status, given_priority, given_name, 
                given_success, dict_effect):
        super().__init__(start_status, given_priority, given_name)
        self.success_rate   = given_success
        self.effect         = dict_effect

    """
    Task Node Constructor
    Purpose:    Initialize the fields of a Task Node
    Arguments:  given_name, the name of the task (string)
                given_success, the success rate of the task (int)
                start_status, the initial state of the task (bool)
                given_priority, the priority of the node (int) 
    Returns:    Nothing
    Effects:    Creates a new Task Node
    Notes:      
    """
    def run(self):
        print("Running Task:", self.name, "...")
        random_chance = random.random() * 100

        if (random_chance < self.success_rate):
            print("Task", [self.name], "Succeeded")
            self.effect()
            self.status = "Succeeded"
            return "Succeeded"
        else:
            print("Task", [self.name], "Failed")
            self.status = "Failed"
            return "Failed"
