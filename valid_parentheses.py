def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    :param s: string to check
    :return: bool
    """

    hash_map = {
        "()": 1,
        "[]": 1,
        "{}": 1,
    }

    for char in s:
        if char == "(":
            hash_map["()"] = 0
        elif char == "[":
            hash_map["[]"] = 0
        elif char == "{":
            hash_map["{}"] = 0
        elif char == ")" and hash_map["()"] != 1:
            hash_map["()"] = 0
        elif char == "]" and hash_map["[]"] != 1:
            hash_map["[]"] = 0
        elif char == "}" and hash_map["{}"] != 1:
            hash_map["{}"] = 0

    if hash_map["()"] == 1 and hash_map["[]"] == 1 and hash_map["{}"] == 1:
        return True
    else:
        return False


def test(expected: bool, actual: bool):
    if expected == actual:
        print("⭕")
    else:
        print(f"❌\nexpected: {expected}\nactual:{actual}")


test(True, valid_parentheses("()"))
test(True, valid_parentheses("()[]{}"))
test(False, valid_parentheses("())[]{}"))
test(False, valid_parentheses("(]"))
test(False, valid_parentheses("([)]"))

