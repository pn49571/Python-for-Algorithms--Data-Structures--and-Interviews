string = "((()))"

def valid_parenthesis(string):
    stack = []
    for i in string:
        if i != ")":
            stack.append(i)
        else:
            if len(stack) != 0:
                peek = stack.pop()
                if peek != "(":
                    return False
            #to test if the ) has come first in the string
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(valid_parenthesis(string))

