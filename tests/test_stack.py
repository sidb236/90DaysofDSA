from Stack import Stack


def test_push_pop_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.traverse() == [1]


def test_peek_and_is_empty():
    stack = Stack()
    assert stack.peek() is None
    assert stack.is_empty()
    stack.push(10)
    assert not stack.is_empty()
    assert stack.peek() == 10
