# test file for app
from app import *

# test functions
def test_total_empty() -> None:
    assert total([]) == 0.0
    
def test_total_single_item() -> None:
    assert total([110.0]) == 110.0
    