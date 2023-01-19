def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    :param s: string to check
    :return: bool
    """

    hash_map = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}

    for char in s:
        # print(char if char == ")" else "S")
        # print(hash_map.get("3", 0))
        # hash_map[char] = hash_map.get(char, 0) + 1
        hash_map[char] += 1

    if hash_map["("] != hash_map[")"]:
        return False
    if hash_map["["] != hash_map["]"]:
        return False
    if hash_map["{"] != hash_map["}"]:
        return False

    return True


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

