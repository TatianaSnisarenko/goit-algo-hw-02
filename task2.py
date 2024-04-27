import string
from collections import deque
import re


def remove_spaces_and_punctuation(text):
    return re.sub(r'[—\s' + re.escape(string.punctuation) + ']', '', text)


def is_palindrom(data: str) -> bool:
    dq = deque()
    text = remove_spaces_and_punctuation(data)
    if len(text) == 0:
        return False
    for c in text.lower():
        dq.append(c)

    while (len(dq) > 1):
        if dq.popleft() != dq.pop():
            return False
    return True
