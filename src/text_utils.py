
"""Utility functions for cleaning and formatting text."""


def clean_name(raw):
    """Collapse whitespace and convert the name to title case."""

    # Collapse whitespace, then title-case
    return " ".join(raw.split()).title()
