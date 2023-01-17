def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    :param nums: list[int]
    :param target: int
    :return: list[int]
    """

    for i, num_1 in enumerate(nums):
        for j, num_2 in enumerate(nums):
            if num_1 + num_2 == target and i != j:
                return [i, j]


def test(expected: list[int], actual: list[int]):
    if sorted(expected) == sorted(actual):
        print("⭕")
    else:
        print(f"❌\nexpected: {expected}\nactual:{actual}")


test([1, 2], two_sum([3, 2, 4], 6))
test([0, 1], two_sum([3, 3], 6))

