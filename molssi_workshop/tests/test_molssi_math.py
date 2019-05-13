

import molssi_workshop  
import pytest

def test_mean():
    """Ensure the mean function works"""
    assert molssi_workshop.mean([17,18,19]) == 18.0
