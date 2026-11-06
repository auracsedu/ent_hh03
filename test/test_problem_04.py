import pytest

from problem_04 import count_n_queens, is_safe, solve_n_queens


@pytest.mark.parametrize(
    "cols, c, expected",
    [
        ([], 0, True),
        ([], 3, True),
        ([0], 0, False),
        ([0], 1, False),
        ([0], 2, True),
        ([1, 3], 0, True),
        ([1, 3], 2, False),
        ([1, 3], 1, False),
        ([1, 3], 3, False),
        ([1, 3, 0], 2, True),
        ([2, 0], 3, True),
        ([2, 0], 1, False),
    ],
)
def test_is_safe(cols, c, expected):
    assert is_safe(cols, c) is expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [[0]]),
        (2, []),
        (3, []),
        (4, [[1, 3, 0, 2], [2, 0, 3, 1]]),
    ],
)
def test_solve_n_queens(n, expected):
    assert solve_n_queens(n) == expected


def test_solve_n_queens_5():
    solutions = solve_n_queens(5)
    assert len(solutions) == 10
    assert solutions[0] == [0, 2, 4, 1, 3]
    assert solutions[-1] == [4, 2, 0, 3, 1]
    assert solutions == sorted(solutions)


def test_solutions_are_valid_and_independent():
    for cols in solve_n_queens(6):
        assert sorted(cols) == [0, 1, 2, 3, 4, 5]
        for r1 in range(6):
            for r2 in range(r1 + 1, 6):
                assert abs(cols[r1] - cols[r2]) != r2 - r1


@pytest.mark.parametrize("n, expected", [(1, 1), (2, 0), (3, 0), (4, 2), (5, 10), (6, 4), (7, 40), (8, 92)])
def test_count_n_queens(n, expected):
    assert count_n_queens(n) == expected
