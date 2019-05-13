

import molssi_workshop  
import pytest


@pytest.mark.myTest
@pytest.mark.label2
@pytest.mark.parametrize("num_list, expectedd_mean", [
    ([1,2,3,4,5], 3),
    ([10,20,30], 20),
    ([1,1,1,1,1,1,1], 1)
])
def test_mean(num_list, expectedd_mean):
    """Ensure the mean function works"""
    assert molssi_workshop.mean(num_list) == expectedd_mean


