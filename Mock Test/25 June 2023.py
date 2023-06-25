# Necessary import
from typing import List, Any

class EmptyStack(ValueError):
    pass

class EmptyQueue(ValueError):
    pass

class StackOverflow(ValueError):
    pass

class QueueOverflow(ValueError):
    pass
'''
Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty. (5 POINTS)
'''
class Stack:

    def __init__(self, maxsize: int = 0, *values: List[Any]):
        self._underlying = []
        for value in values:
            self._underlying.append(value)
        self.max_size = maxsize

    def size(self) -> int:
        return len(self._underlying)

    def peek(self) -> Any:
        if not self._underlying:
            return self._underlying[-1]
        raise EmptyStack('Stack has no elements')
    top = peek

    def is_empty(self) -> bool:
        return not self._underlying

    def clear(self) -> None:
        self._underlying = []

    def push(self, element: Any) -> None:
        if self.max_size and len(self._underlying) >= self.max_size:
            raise StackOverflow('Stack has reached it\'s maximum size')
        self._underlying.append(element)

    def pop(self) -> None:
        if self.is_empty():
            raise EmptyStack('Stack has no elements')

    def search(self, element: Any) -> Any:
        if self.is_empty():
            raise EmptyStack('Stack has no elements')

        for i, item in enumerate(self._underlying, start = 0):
            if item == element:
                return i

        else:
            raise ValueError('Item not found in Stack!')

    def __iter__(self):
        return self._underlying.__iter__()
    iterator = __iter__

'''
Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty. (5 POINTS)
'''
class Queue:

    def __init__(self, maxsize: int = 0, *values: List[Any]) -> None:
        self._underlying = []
        for value in values:
            self._underlying.append(value)
        self.max_size = maxsize

    def enqueue(self, element: Any) -> bool:
        if self.max_size and len(self._underlying) >= self.max_size:
            raise QueueOverflow('Queue has reached it\'s maximum size')
        self._underlying.insert(0, element)
        return True

    def dequeue(self, element: Any) -> Any:
        if not self._underlying:
            raise EmptyQueue('Queue has no elements')
        return self._underlying.pop()

    def peek(self) -> Any:
        if not self._underlying:
            return self._underlying[-1]
        raise EmptyQueue('Queue has no elements')
    front = peek

    def is_empty(self) -> bool:
        return not self._underlying

    def clear(self) -> None:
        self._underlying = []

    def size(self) -> int:
        return len(self._underlying)

    def __iter__(self):
        return self._underlying.__iter__()
    iterator = __iter__
