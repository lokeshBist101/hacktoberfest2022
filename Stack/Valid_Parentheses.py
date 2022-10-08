def isValid(s):
    length = len(s)
    stack = []
    for i in range(length):
        if s[i] == '[' or s[i] == '{' or s[i] == '(':
            stack.append(s[i])
        elif s[i] == ']' or s[i] == '}' or s[i] == ')':
            if stack:
                if s[i] == ')' and stack[-1] == '(' or s[i] == '}' and stack[-1] == '{' or s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
    return len(stack) == 0