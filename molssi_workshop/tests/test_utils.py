import molssi_workshop
import pytest


def test_title_case():
    """test the title case function"""
    assert title_case('hello world!') == 'Hello World!'
