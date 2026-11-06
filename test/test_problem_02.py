import pytest

from problem_02 import deep_reverse, flatten_with_depth, max_depth


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], 1),
        ([], 1),
        ([1, [2, 3], 4], 2),
        ([1, [2, [3, [4]]]], 4),
        ([[], [[]], []], 3),
        ([[1], [2], [3]], 2),
        ([1, [2], [[3]], [[[4]]]], 4),
    ],
)
def test_max_depth(items, expected):
    assert max_depth(items) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], [3, 2, 1]),
        ([1, [2, 3], 4], [4, [3, 2], 1]),
        ([[1, 2], [3, [4, 5]]], [[[5, 4], 3], [2, 1]]),
        ([], []),
        ([[]], [[]]),
        ([1, [2, [3, [4]]]], [[[[4], 3], 2], 1]),
        ([[1], 2, [3]], [[3], 2, [1]]),
    ],
)
def test_deep_reverse(items, expected):
    assert deep_reverse(items) == expected


def test_deep_reverse_makes_a_new_list():
    items = [1, [2, 3], 4]
    result = deep_reverse(items)
    assert items == [1, [2, 3], 4]
    assert result is not items
    assert result[1] is not items[1]


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], [(1, 1), (2, 1), (3, 1)]),
        ([1, [2, [3]], 4], [(1, 1), (2, 2), (3, 3), (4, 1)]),
        ([[], [[]], []], []),
        ([], []),
        ([[1, 2], [3, [4, 5]]], [(1, 2), (2, 2), (3, 2), (4, 3), (5, 3)]),
        ([[[7]]], [(7, 3)]),
    ],
)
def test_flatten_with_depth(items, expected):
    assert flatten_with_depth(items) == expected


def test_original_is_not_changed():
    items = [1, [2, [3]], 4]
    max_depth(items)
    flatten_with_depth(items)
    assert items == [1, [2, [3]], 4]
