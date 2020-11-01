################################################################################
#  Tufts University COMP 131, Summer 2020                                      #
#  Roomba.py                                                                   #
#  By:          Sawyer Bailey Paccione                                         #
#  Completed:                                                                  #
#                                                                              #
#  Description: A behavior tree of Task Nodes, Condition Nodes, Composite      #
#               Nodes and Decoratore Nodes. These nodes describe the           #
#               the actions of a Roomba (*See BT.pdf)                          #
#  Purpose:     Clean up the dirt                                              #
################################################################################

from Blackboard import Blackboard

from Node import Node
from Task import Task
from Condition import Condition
from Priority import Priority
from Sequence import Sequence
from Selector import Selector
from Decorator import Timer
from Decorator import UntilFail
from Decorator import Negate

import time

class Roomba:
    
    """
    Roomba Constructor
    Purpose:    Clean Up the House based on a behavior Tree
    Arguments:  given_blackboard [Blackboard], 
    Returns:    Nothing
    Effects:    [Memory] Creates an object
    Notes:      
    """
    def __init__(self, given_blackboard):
        self.blackboard     = given_blackboard
        self.success_rate   = 100


    """
    build_tree
    Purpose:    Build a pre-defined tree for the Roomba in a Pre-Order Traversal
    Arguments:  Nothing, it is self sufficient since the tree is predefined
    Returns:    Nothing
    Effects:    [Memory] Creates many objects
                [Connections] Between Nodes
    Notes:      
    """
    def build_tree(self):        
        #Leftchild
        parent      = Sequence("Failed", 1)

        battery     = Condition("Failed", -1, "Battery < 30%", self.battery_low)
        find_home   = Task("Failed", -1, "Find Home", self.success_rate, 
                            self.write_to_HomePath)
        go_home     = Task("Failed", -1, "GO HOME", self.success_rate,
                            self.read_from_HomePath)
        dock        = Task("Failed", -1, "DOCK", self.success_rate, 
                            self.no_effect)

        self.build_subtree(parent, battery, find_home, go_home, dock)

        #Center Child
        #Level 6
        parent6 = Sequence("Failed", -1)

        dusty_con = Condition("Failed", -1, "Dusty Spot", self.dusty_spot)
        clean_task = Task("Failed", -1, "Clean Spot", self.success_rate, 
                            self.no_effect)
        decorator_time = Timer("Failed", -1, clean_task, 35)
        self.build_subtree(parent6, dusty_con, decorator_time)

        #Level 5
        parent5     = Selector("Failed", -1)
        
        clean_task2 = Task("Failed", -1, "Clean", self.success_rate, 
                            self.no_effect)

        self.build_subtree(parent5, parent6, clean_task2)

        #Level 4
        parent4 = Sequence("Failed", -1)
        battery_2  = Condition("Failed", -1, "Battery < 30%", self.battery_low)
        decorator_negate = Negate("Failed", -1, battery_2)

        self.build_subtree(parent4, decorator_negate, parent5)

        #Level 3
        parent3 = Sequence("Failed", -1)
        dec_untilfail = UntilFail("Failed", -1, parent4)
        done_general = Task("Failed", -1, "Done General", self.success_rate,
                            self.effect_general)

        self.build_subtree(parent3, dec_untilfail, done_general)

        #Level 2
        
        #Left
        parent2a = Sequence("Failed", -1)
        spot_con = Condition("Failed", -1, "Spot", self.spot_condition)
        
        clean_task3 = Task("Failed", -1, "Clean Spot", self.success_rate, 
                            self.no_effect)
        decorator_time2 = Timer("Failed", -1, clean_task3, 20)

        spot_task = Task("Failed", -1, "Done Spot", self.success_rate, 
                          self.effect_spot)

        self.build_subtree(parent2a, spot_con, decorator_time2, spot_task)
        
        #Right
        parent2b = Sequence("Failed", -1)
        general_con = Condition("Failed", -1, "General", self.general_condition)
    
        self.build_subtree(parent2b, general_con, parent3)

        #Level 1
        parent1 = Selector("Failed", 2)

        self.build_subtree(parent1, parent2a, parent2b)

        #Right Child
        nothing_task = Task("Failed", 3, "Do Nothing", self.success_rate, 
                            self.no_effect)

        #Root 
        self.behavior_tree_root = Priority("Failed", -1)

        self.build_subtree(self.behavior_tree_root, parent, parent1,
        nothing_task)

    """
    startup
    Purpose:    Initiates values in the behavior tree
    Arguments:  Nothing
    Returns:    Nothing
    Effects:    Game Mode
    Notes:      
    """
    def run(self):
        drain_rate      = int(input("Drainage of Batter Per Turn? (0 - 100) "))
        task_success    = int(input("Task Success Rate? (0 - 100) "))
        
        self.success_rate = task_success

        self.build_tree()

        print("Here is the Behavior Tree of this Roomba: ")
        self.behavior_tree_root.print_subtree()

        while True:
            self.behavior_tree_root.run()
            time.sleep(2)
            self.blackboard.dict["BATTERY"] -= drain_rate
            # Reset Battery as if the Roomba charged
            if (self.blackboard.dict["BATTERY"] < 0):
                self.blackboard.dict["BATTERY"] = 100




    """
    interactive
    Purpose:    Interactive game_mode that lets the user initiate values
    Arguments:  Nothing
    Returns:    Nothing
    Effects:    Values in dictionary and success rates
    Notes:      
    """
    def interactive(self):
        pass
    
    """
    automatic
    Purpose:    Automatic game_mode that automatically sets various values
    Arguments:  Nothing
    Returns:    Northing
    Effects:    Values in dictionary and success rates
    Notes:      
    """
    def automatic(self):
        pass

    """
    build_subtree
    Purpose:    Given a parent and children put them together
    Arguments:  parents  [Node] A parent node (usually a composite)
                children [Node] A variable number of children
    Returns:    Nothing
    Effects:    Children Field of parent Node
    Notes:      
    """
    def build_subtree(self, parent, *children):
        for child in children:
            parent.add_child(child)

    ############################################################################
    #                         Condition Functions                              #
    ############################################################################
    """
    battery_low
    Purpose:    Function for the Battery Condition to determine Success or 
                Failure
    Arguments:  Nothing
    Returns:    The result of the condition 
    Effects:    The success or the Condition Node
    Notes:      
    """
    def battery_low(self):
        if (self.blackboard.dict.get("BATTERY") < 30):
            return "Succeeded"
        else:
            return "Failed"

    """
    dusty_spot
    Purpose:    Function for the Dusty Spot Condition to determine Success
                or Failure
    Arguments:  Nothing
    Returns:    The result of the condition check
    Effects:    The status of the Condition Node
    Notes:      
    """    
    def dusty_spot(self):
        if (self.blackboard.dict.get("DUSTY")):
            return "Succeeded"
        else:
            return "Failed"

    """
    general_condition
    Purpose:    Function for the general condition to determine Success
                or Failure
    Arguments:  Nothing
    Returns:    The result of the Condition check
    Effects:    The status of the Condition Node
    Notes:      
    """
    def general_condition(self):
        if (self.blackboard.dict.get("GENERAL")):
            return "Succeeded"
        else:
            return "Failed"

    """
    spot_condition
    Purpose:    Function for the spot condition to determine Success
                or Failure
    Arguments:  Nothing
    Returns:    The result of the condition check
    Effects:    The status of the condition node
    Notes:      
    """
    def spot_condition(self):
        if (self.blackboard.dict.get("SPOT")):
            return "Succeeded"
        else:
            return "Failed"

    ############################################################################
    #                            Task Functions                                #
    # Tasks sometimes impact a value in the blackboard, these functions are    #
    # those value updates                                                      #
    ############################################################################
    """
    no_effect
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def no_effect(self):
        pass

    """
    write_to_HomePath
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def write_to_HomePath(self):
        print("Writing to HOMEPATH dictionary entry")
        self.blackboard.dict["HOME"] = "New Home Path"

    """
    read_from_HomePath
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def read_from_HomePath(self):
        print("Reading from HOMEPATH dictionary entry")
        self.blackboard.dict["HOME"] = "New Home Path"

    """
    effect_general
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """    
    def effect_general(self):
        print("Setting Corresponding Value to False")
        self.blackboard.dict["GENERAL"] = False

    """
    effect_spot
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def effect_spot(self):
        print("Setting Corresponding Value to False")
        self.blackboard.dict["SPOT"]    = False