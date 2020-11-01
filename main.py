#  Tufts University COMP 131, Summer 2020
#  main.py
#  By:          Sawyer Bailey Paccione
#  Completed:   
#  
#  Description: A behavior tree of Task Nodes, Condition Nodes, Composite
#               Nodes and Decoratore Nodes. These nodes describe the 
#               the actions of a Roomba (*See BT.pdf)
#  Purpose:     Clean up the dirt

from Roomba import Roomba
from Blackboard import Blackboard

"""
create_blackboard
Purpose:    Interact witt the user in terminal, initiate the Blackboard
Arguments:  Nothing
Returns:    The newly created blackboard
Effects:    The blackboard members
Notes:      
"""
def create_blackboard():
    print("Welcome to Roomba Testing")
    game_mode = input("Would you like to set up the simulation? (Y/N) ")
    game_mode = game_mode.upper()

    while (game_mode == "" or game_mode[0] != "N" and game_mode[0] != "Y"):
        print(game_mode, "Is not a valid input")
        print("Please Only input 'Y' or 'N'")
        game_mode = input("Setup blackboard? (Y/N) ")
        game_mode = game_mode.upper()
    
    if(game_mode[0] == "Y"):
        return interactive()
    else:
        return automatic()

"""
interactive
Purpose:    Interactively set initially blackboard values
Arguments:  Nothing
Returns:    The blackboard
Effects:    create_blackboard
"""
def interactive():
    battery         = int(input("Starting Battery Level? (0 - 100) "))
    inter_bb        = Blackboard(battery, False, False, False, "HOMEPATH")
    return inter_bb

"""
automatic
Purpose:    Automatically set initially blackboard values
Arguments:  Nothing
Returns:    The blackboard
Effects:    create_blackboard  
"""
def automatic():
    auto_bb         = Blackboard(100, False, False, False, "HOMEPATH")
    return auto_bb


kevin_blackboard = create_blackboard()
kevin = Roomba(kevin_blackboard)
kevin.run()