import copy

import pytest

from problem_05 import find_empty, is_valid, solve

PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
SOLUTION = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def blanked(board, cells):
    board = copy.deepcopy(board)
    for r, c in cells:
        board[r][c] = 0
    return board


def test_find_empty():
    assert find_empty(PUZZLE) == (0, 2)
    assert find_empty(SOLUTION) is None
    assert find_empty(blanked(SOLUTION, [(8, 8)])) == (8, 8)
    assert find_empty(blanked(SOLUTION, [(3, 4), (2, 7)])) == (2, 7)


@pytest.mark.parametrize(
    "r, c, d, expected",
    [
        (0, 2, 4, True),
        (0, 2, 5, False),  # 같은 행
        (0, 2, 8, False),  # 같은 상자 (2, 2)
        (0, 2, 9, False),  # 같은 상자 (2, 1)
        (0, 2, 1, True),
        (4, 4, 5, True),
        (4, 4, 6, False),  # 같은 열 (3, 4)
        (4, 4, 4, False),  # 같은 행 (4, 0)
        (4, 4, 2, False),  # 같은 상자 (5, 4)
        (8, 0, 3, True),
        (8, 0, 7, False),  # 같은 열 (5, 0)
    ],
)
def test_is_valid(r, c, d, expected):
    assert is_valid(PUZZLE, r, c, d) is expected


def test_solve_full_puzzle():
    board = copy.deepcopy(PUZZLE)
    assert solve(board) is True
    assert board == SOLUTION


def test_solve_already_complete():
    board = copy.deepcopy(SOLUTION)
    assert solve(board) is True
    assert board == SOLUTION


def test_solve_few_blanks():
    board = blanked(SOLUTION, [(0, 0), (0, 1), (1, 0), (4, 4), (8, 8)])
    assert solve(board) is True
    assert board == SOLUTION


def test_unsolvable_leaves_board_unchanged():
    # (0, 8) 에 들어갈 수 있는 숫자가 없는 판: 행에 1~8, 열에 9
    board = [[0] * 9 for _ in range(9)]
    board[0] = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    board[1][8] = 9
    before = copy.deepcopy(board)
    assert solve(board) is False
    assert board == before


def test_unsolvable_after_some_backtracking():
    # 앞쪽 빈칸 몇 개를 채워 본 뒤에야 막히는 판
    board = copy.deepcopy(SOLUTION)
    board[0][0] = 0
    board[0][1] = 0
    board[1][0] = 0
    board[8][8] = 0
    board[7][8] = 9  # (8, 8) 에 9 가 들어가야 하는데 같은 열에 9 가 생김
    before = copy.deepcopy(board)
    assert solve(board) is False
    assert board == before
