from collections import deque
import re


class Stack():
    def __init__(self) -> None:
        self.stack = deque()

    def put(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def get_brackets(data: str) -> str:
    return re.sub(r"[^\(\){}\[\]]", "", data)


def is_open(bracket: str) -> bool:
    open_brackets = {'[', '(', '{'}
    return bracket in open_brackets


def is_symmetrical(data: str) -> bool:
    pairs = {']': '[', ')': '(', '}': '{'}
    brackets = get_brackets(data)
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False
    stack = Stack()
    for bracket in brackets:
        if is_open(bracket):
            stack.put(bracket)
        else:
            if stack.is_empty():
                return False
            else:
                if (stack.pop() != pairs[bracket]):
                    return False
    return True
