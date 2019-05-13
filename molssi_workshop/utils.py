"""
utils.py
A file containing utility functions.
"""


def title_case(sentence):
    """
    Convert a string into a title case.
    
    Title case means that the first letter of each 
    word is a capitalized with all other letters
    in lower case

    Parameters
    ----------
    sentence: str
        String to be converted into title case.
    
    Returns
    -------

    title : str
        String in title case format

    Example
    -------
    >>> title_case('hElLo WoRlD!')
    'Hello World!'
    """

    words = sentence.split(' ')
    title = ""
    for word in words:
        title = title + word[0].upper() + word[1:].lower() + " "
    return(title)















