def isValid(self, s: str) -> bool:
    loop = []
    for c in s:
        if c in ['(', '{', '[']:
            loop.append(c)
        elif c == ')' and len(loop) != 0 and loop[-1] == '(':
            loop.pop()
        elif c == ']' and len(loop) != 0 and loop[-1] == '[':
            loop.pop()
        elif c == '}' and len(loop) != 0 and loop[-1] == '{':
            loop.pop()
        else:
            return False
    return loop == []