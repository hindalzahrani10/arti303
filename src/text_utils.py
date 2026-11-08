"""Utilities for cleaning text."""

def clean_name(raw):
    """Clean and format a name."""
    # TODO: collapse whitespace, then title-case
    return " ".join(raw.split()).title()
