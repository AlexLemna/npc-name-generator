import textwrap

def printw(x): 
    '''Textwrapping for regular 'print' commands.'''
    print ( textwrap.fill (x, width = 70))

def inputw(x): 
    '''Textwrapping for user input prompts.'''
    _input = input ( textwrap.fill (x, width=70))
    return ( _input )