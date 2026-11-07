"""Tests for src/text_utils.py"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import text_utils


def test_clean_name_whitespace():
    """Test that extra whitespace is removed."""
    assert text_utils.clean_name("  john    smith  ") == "John Smith"
    


def test_clean_name_capitalisation():
    """Test that names are correctly capitalised."""
    assert text_utils.clean_name("JOHN SMITH") == "John Smith"
    assert text_utils.clean_name("jane doe") == "Jane Doe"
    
