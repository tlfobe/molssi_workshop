"""
Unit and regression test for the molssi_workshop package.
"""

# Import package, test suite, and other packages as needed
import molssi_workshop
import pytest
import sys

def test_molssi_workshop_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molssi_workshop" in sys.modules
