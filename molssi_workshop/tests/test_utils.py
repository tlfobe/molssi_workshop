import molssi_workshop
import pytest


def test_title_case():
    """test the title case function"""
    assert molssi_workshop.title_case('hello world!') == 'Hello World! '

def test_type_error():
    pass 
