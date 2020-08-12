from time import sleep
from dep import is_4k

def is_windows():    
    # This sleep could be some complex operation instead
    sleep(5)    
    return True  

def get_operating_system():    
    return 'Windows' if is_windows() else 'Linux'

def get_resolution():
    return '4K' if is_4k() else 'Standard'