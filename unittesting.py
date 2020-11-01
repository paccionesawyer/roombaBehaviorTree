#  Tufts University COMP 131, Summer 2020
#  main.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: A behavior tree of Task Nodes, Condition Nodes, Composite
#               Nodes and Decoratore Nodes. These nodes describe the 
#               the actions of a Roomba (*See BT.pdf)
#  Purpose:     Clean up the dirt

import unittest

from Task import Task
from Condition import Condition
from Priority import Priority
from Sequence import Sequence
from Selector import Selector
from Decorator import Timer
from Decorator import UntilFail
from Decorator import Negate

class TestTaskMethods(unittest.TestCase):
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def no_effect(self):
        return
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def condition_function(self):
        return "Succeeded"

    #Testing Task
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """    
    def test_TaskPrint(self):
        self.testing_task = Task("Failed", -1, "Testing Task Node", 100, 
                                 self.no_effect)     
        self.assertEqual(self.testing_task.run(), "Succeeded")   

    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """        
    def test_TaskSuccess(self):
        self.testing_task = Task("Failed", -1, "Testing Task Node", 100, 
                                 self.no_effect) 
        self.testing_task.run() 
        self.assertEqual(self.testing_task.status, "Succeeded")
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def test_Condition(self):
        print("testing_Condition")
        testing_condition = Condition("Failed", -1, "Testing Condition Node", 
                                      self.condition_function)
        self.assertEqual(testing_condition.run(), "Succeeded")
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def test_Selector(self):
        testing_task1 = Task("Failed", -1,"Testing Task Node1", 0, self.
                            no_effect)
        testing_task2 = Task("Failed", -1, "Testing Task Node2", 0, self.
                            no_effect)
        testing_task3 = Task("Failed", -1, "Testing Task Node3", 100, self.
                            no_effect)

        testing_Selector = Selector("Failed", -1)
        testing_Selector.add_child(testing_task1)
        testing_Selector.add_child(testing_task2)
        testing_Selector.add_child(testing_task3)

        self.assertEqual(testing_Selector.run(), "Succeeded")
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def test_Sequence(self):
        testing_task1 = Task("Failed", -1,"Testing Task Node1", 100, self.
                            no_effect)
        testing_task2 = Task("Failed", -1, "Testing Task Node2", 0, self.
                            no_effect)
        testing_task3 = Task("Failed", -1, "Testing Task Node3", 100, self.
                            no_effect)

        testing_Sequence = Sequence("Failed", -1)
        testing_Sequence.add_child(testing_task1)
        testing_Sequence.add_child(testing_task2)
        testing_Sequence.add_child(testing_task3)

        self.assertEqual(testing_Sequence.run(), "Failed")
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def test_Priority(self):
        testing_task1 = Task("Failed", 3, "Testing Task Node1", 0, self.
                            no_effect)
        testing_task2 = Task("Failed", 1, "Testing Task Node2", 0, self.
                            no_effect)
        testing_task3 = Task("Failed", 2, "Testing Task Node3", 100, self.
                            no_effect)  

        testing_Priority = Priority("Failed", -1)
        testing_Priority.add_child(testing_task1)
        testing_Priority.add_child(testing_task2)
        testing_Priority.add_child(testing_task3)

        self.assertEqual(testing_Priority.run(), "Succeeded")
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    def test_Negation(self):
        testing_task1 = Task("Failed", -1, "Testing Task Node1", 100, self.
                            no_effect)

        testing_task2 = Task("Failed", -1, "Testing Task Node1", 0, self.
                            no_effect)

        testing_Negation = Negate("Failed", -1, testing_task1)
        testing_Negation2 = Negate("Failed", -1, testing_task2)

        self.assertEqual(testing_Negation.run(), "Failed")
        self.assertEqual(testing_Negation2.run(), "Succeeded")
    
    """
    funcname
    Purpose:    
    Arguments:  
    Returns:    
    Effects:    
    Notes:      
    """
    # def test_UntilFail(self):
    #     testing_task1 = Task("Failed", -1, "Testing Task Node1", 50, self.
    #                         no_effect)

    #     testing_UF = UntilFail("Failed", -1, testing_task1)

    #     testing_UF.run()

    def test_conditional_execution(self, parameter_list):
        pass

if __name__ == '__main__':
    unittest.main()
