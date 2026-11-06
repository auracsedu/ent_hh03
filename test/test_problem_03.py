import pytest

from problem_03 import count_change, generate_parentheses


@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (0, [1, 2], 1),
        (0, [], 1),
        (4, [1, 2], 3),
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (3, [], 0),
        (10, [10], 1),
        (10, [2, 5, 3, 6], 5),
        (100, [1, 5, 10, 25, 50], 292),
        (7, [7, 1], 2),
    ],
)
def test_count_change(amount, coins, expected):
    assert count_change(amount, coins) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, [""]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ],
)
def test_generate_parentheses(n, expected):
    assert generate_parentheses(n) == expected


def test_generate_parentheses_counts():
    # 카탈란 수: 1, 1, 2, 5, 14, 42, 132
    assert [len(generate_parentheses(n)) for n in range(7)] == [1, 1, 2, 5, 14, 42, 132]


def test_generate_parentheses_all_balanced():
    for s in generate_parentheses(5):
        depth = 0
        for ch in s:
            depth += 1 if ch == "(" else -1
            assert depth >= 0
        assert depth == 0
