import pytest
from array import array

from array_ds import (
    traverse_array,
    insert_element,
    access_element,
    linear_search,
    delete_element,
)


def test_insert_and_traverse():
    arr = array('i', [1, 2, 3])
    insert_element(arr, 1, 9)
    assert traverse_array(arr) == [1, 9, 2, 3]


def test_delete_element():
    arr = array('i', [1, 2, 3])
    delete_element(arr, 2)
    assert traverse_array(arr) == [1, 3]


def test_access_element():
    arr = array('i', [1, 2, 3])
    assert access_element(arr, 1) == 2


def test_access_element_out_of_range():
    arr = array('i', [1, 2, 3])
    with pytest.raises(IndexError):
        access_element(arr, 5)


def test_linear_search():
    arr = array('i', [1, 2, 3])
    assert linear_search(arr, 3) == 2
    assert linear_search(arr, 4) == -1
