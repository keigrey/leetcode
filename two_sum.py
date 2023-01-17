def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    :param nums: list[int]
    :param target: int
    :return: list[int]
    """

    hash_map = {}

    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [i, hash_map[target - num]]
        hash_map[num] = i


def test(expected: list[int], actual: list[int]):
    if sorted(expected) == sorted(actual):
        print("⭕")
    else:
        print(f"❌\nexpected: {expected}\nactual:{actual}")


test([1, 2], two_sum([3, 2, 4], 6))
test([0, 1], two_sum([3, 3], 6))

