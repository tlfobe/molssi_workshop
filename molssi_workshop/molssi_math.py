"""
molssi_math.py
A package developed in the MolSSI workshop to do... math

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def mean(mylist):
    """
    function to take the mean of a list
    
    Parameters
    ----------
    mylist : list
        list of numbers to take a mean
    
    
    Returns
    -------
    mean_list : float
        The mean of the list.


    Examples
    --------
    >>> mean([1,2,3,4,5,6,7])
    4.0


    """
    if not isinstance(mylist, list):
        raise TypeError("Mean: %s is not a list!" % mylist)

    return (sum(mylist) / len(mylist))


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
