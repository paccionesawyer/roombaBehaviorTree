#  Tufts University COMP 131, Summer 2020
#  Blackboard.py
#  By:          Sawyer Bailey Paccione
#  Completed:
#  
#  Description: Blackboard Object for a Roomba's Decision Tree, made up of a    
#               dictionary (Hash Table) with a Battery Life, Spot, General, 
#               Dusty Spot, Home_Path
#  Purpose:     Represent the current state of the environment of the Roomba

class Blackboard:

    """    
    Blackboard Constructor
    Purpose:    An inter-task communication method
    Arguments:  batter_level[int], an integer number between 0 and 100
                spot        [bool], TRUE if the command was requested, FALSE 
                otherwise
                general     [bool], TRUE if the command was requested, FALSE 
                dusty_spot  [bool], TRUE if the sensor detected a dusty spot 
                during the cycle, FALSE otherwise
                home_path   [PATH],  The path to the docking station
    Returns:    Nothing
    Effects:    Creates a blackboard object
    Notes:      
    """  
    def __init__(self, battery_level, spot, general, dusty_spot, home_path):
        self.dict = {'BATTERY': battery_level, 'SPOT': spot, 'GENERAL': general, 'DUSTY': dusty_spot, 'HOME': home_path}

