from array import array


def traverse_array(arr):
    """Return elements of ``arr`` as a list for traversal verification."""
    return [i for i in arr]


def insert_element(arr, index, value):
    """Insert ``value`` at ``index`` in ``arr`` and return the array."""
    arr.insert(index, value)
    return arr


def access_element(arr, index):
    """Return the element at ``index`` from ``arr``.

    Raises:
        IndexError: If ``index`` is out of bounds.
    """
    if index >= len(arr):
        raise IndexError("The index provided exceeds the length of array")
    return arr[index]


def linear_search(arr, target):
    """Return the index of ``target`` in ``arr`` using linear search or -1."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def delete_element(arr, target):
    """Delete the first occurrence of ``target`` from ``arr`` and return it."""
    try:
        arr.remove(target)
    except ValueError:
        pass
    return arr


if __name__ == "__main__":
    # Demonstration of functions (not executed when imported)
    arr1 = array('i', [1, 2, 3, 4, 5])
    print(traverse_array(arr1))
    insert_element(arr1, 0, 7)
    print(arr1)
    print(access_element(arr1, 2))
    print(linear_search(arr1, 4))
    delete_element(arr1, 3)
    print(arr1)
