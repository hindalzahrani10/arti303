"""TODO: describe what this module is for."""
"""Utility functions for converting GPA to letter grades."""

def letter_grade(gpa):
    """TODO: describe what this function does."""
    """Return the letter grade for a given GPA on a 5.00 scale."""


    # TODO: your if/elif chain here
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
    pass
