################################################################################
#  Tufts University COMP 131, Summer 2020                                      #
#  README                                                                      #
#  By:          Sawyer Bailey Paccione                                         #
#  Completed:                                                                  #
#                                                                              #
#  Description: A README file contains information about other files in a      #
#               directory or archive of compute software.                      #
################################################################################
            

## Program Purpose                             

This new type of Roomba has very simple reflex rules. It will always check the 
battery level first. If the level is below 30%, it will plan a path to its 
charging base (“home”), go there, and start the docking procedure. If the
battery is at a sufficient level, it will start the function it was commanded 
to perform. The available commands are:
    - Spot cleaning: it will perform a 20s intensive cleaning in a specific area
    - General cleaning: go around the room and vacuum dust until the battery 
      falls under 30%
    - Do nothing


## Acknowledgements 
        
I am new to python, I have a decent amount of experience coding in C, C++. As
such, I visited various websites in trying to determine the best ways to 
implement ideas that would be easy for me to implement in C++. 


## Files


- Blackboard.py [Class]
    - An inter-task communication mechanism. It is made up of a hash-table 
      (dictionary), the key is the variable name and the value is the variable 
      name.

- Node.py [Parent Class]
    - Simple Node class to represent the values in a behavior tree, as a list of
      children

    - Condition.py [Child Class]
        - A condition tests some property of the system

    - Decorator.py [Child Class]
        - Contains three different types of decorators 
            - Logical Negation: It executes the attached node and then it 
              negates its result
            - Until Fail: It executes the attached node until it fails
            - Timer: It executes the attached node for a specific amount of time

    - Selector.py [Child Class]
        - Children are evaluated in order (left to right). It fails if all 
          children have failed, otherwise it succeeds

    - Sequence.py [Child Class]
        - Children are evaluated in order (left to right). It fails as soon as 
          one of the children fails, otherwise it succeeds

    - Task.py [Child Class]
        - A task alters the state of the system

- Roomba.py [Class]
    - A behavior tree made up of nodes

- main.py
    - Creates a blackboard and passes it to the Roomba constructor


## Other Data Structures

List
    - A collection which is ordered and changeable. Allows duplicate members.

Dictionary
    - A collection which is unordered, changeable and indexed. No duplicate 
      members. Like a HashTable


## Testing

A Unit Testing file is provided, in addition running the program helped 
understand the functionality of Until Fail and Timer
