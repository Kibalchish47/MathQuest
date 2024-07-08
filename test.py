import sys
import msvcrt

def clear_console(): 
    sys.stdout.write("\033c")
    sys.stdout.flush()
    
def move_stickman(x, y): 
    clear_console()
    