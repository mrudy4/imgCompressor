import sys

def is_virtualenv():
    '''
    Check if the current Python environment is a virtual environment.
    Returns True if it is a virtual environment, False otherwise.
    '''
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)