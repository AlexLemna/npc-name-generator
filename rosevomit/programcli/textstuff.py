import textwrap


def printwrap(x, indented=False, end_with='\n'):
    """Textwrapping for regular 'print' commands."""
    if indented is True:
        print (textwrap.fill (x, width=70, subsequent_indent="   "), end=end_with)
    else:
        print (textwrap.fill (x, width=70), end=end_with)
