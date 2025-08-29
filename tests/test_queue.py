from q import Queue


def test_add_remove_order():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert queue.remove() == 1
    assert queue.remove() == 2
    assert queue.traverse() == [3]


def test_remove_empty():
    queue = Queue()
    assert queue.remove() is None
    assert queue.is_empty()
