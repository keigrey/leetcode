def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    :param s: string to check
    :return: bool
    """
    stack = []
    closing = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in closing:
            if stack and stack[-1] == closing[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False


def test(expected: bool, actual: bool):
    if expected == actual:
        print("⭕")
    else:
        print(f"❌\nexpected: {expected}\nactual:{actual}")


test(False, valid_parentheses(")("))
test(True, valid_parentheses("()"))
test(True, valid_parentheses("()[]{}"))
test(False, valid_parentheses("())[]{}"))
test(False, valid_parentheses("(]"))
test(False, valid_parentheses("([)]"))

