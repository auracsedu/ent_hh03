"""
[도전] 문제 5. 스도쿠 풀기 (함수 3개)

9 x 9 스도쿠를 백트래킹으로 푸는 함수들을 작성하세요. 판 board 는 정수 9 개씩 담은
리스트 9 개로 된 2차원 리스트이고, 빈칸은 0 입니다. 2주차 어려운 세트 문제 4 에서는
"후보가 하나뿐인 칸"만 채웠지만, 이번에는 후보가 여럿인 칸도 하나씩 넣어 보고
안 되면 되돌리는 방식으로 끝까지 풉니다.

find_empty(board)
- 빈칸(0) 중 가장 먼저 나오는 칸의 (행, 열) 튜플을 돌려줍니다. 행을 위에서부터,
  한 행 안에서는 왼쪽부터 봅니다. 빈칸이 없으면 None 을 돌려줍니다.

is_valid(board, r, c, d)
- 비어 있는 (r, c) 칸에 숫자 d 를 넣어도 되는지 돌려줍니다. 같은 행, 같은 열,
  같은 3 x 3 상자 안에 d 가 이미 있으면 False, 아니면 True 입니다.

solve(board)
- board 를 **제자리에서** 완성하고 True 를 돌려줍니다. 풀 수 없으면 False 를
  돌려주고, 이때 board 는 solve 를 부르기 전과 **똑같은 상태**여야 합니다. (넣어 봤던
  숫자가 남아 있으면 안 됩니다)
- 빈칸이 없는 판은 그대로 True 입니다.
- 테스트의 판은 답이 하나뿐이거나 풀 수 없는 판입니다.

예시
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             ...]
    find_empty(board)        -> (0, 2)
    is_valid(board, 0, 2, 4) -> True
    is_valid(board, 0, 2, 5) -> False    # 같은 행에 5
    is_valid(board, 0, 2, 8) -> False    # 같은 상자에 8
    solve(board)             -> True     # board 가 완성된 판으로 바뀜

재귀로 생각하는 법
    solve 는 "빈칸 하나를 골라 가능한 숫자를 넣어 보고, 나머지는 solve 에 맡긴다"
    입니다.

        1) find_empty 가 None 이면 다 채웠습니다. True.
        2) 그 칸 (r, c) 에 대해 d 를 1 부터 9 까지 돌면서 is_valid 인 d 마다
               board[r][c] = d
               solve(board) 가 True 면 그대로 True 를 돌려준다   <- 되돌리지 않습니다
               아니면 board[r][c] = 0                             <- 되돌립니다
        3) 아홉 숫자가 모두 실패하면 False.

    문제 4 의 append / pop 이 여기서는 board[r][c] = d / board[r][c] = 0 입니다.
    되돌리기를 빠짐없이 하기 때문에, 전체가 실패하면 판은 저절로 원래대로 돌아갑니다.

힌트
    - (r, c) 가 속한 3 x 3 상자의 왼쪽 위 칸은 (r // 3 * 3, c // 3 * 3) 입니다.
      거기서 3 x 3 을 이중 for 로 돌면 상자 안 숫자를 전부 봅니다.
    - is_valid 에서 (r, c) 자신은 비어 있다고 보장되므로 건너뛰지 않아도 됩니다.
    - find_empty 는 이중 for 안에서 0 을 찾는 즉시 return (r, c) 하세요. for 가 다
      끝났으면 None 입니다.
    - 테스트의 판은 백트래킹으로 1초 안에 풀립니다. 오래 걸리면 is_valid 가 틀린
      숫자를 통과시키고 있는 것입니다.
    - 풀 수 없는 판 테스트는 solve 뒤에 판이 그대로인지 확인합니다. 2) 에서 실패했을
      때 0 으로 되돌리는 줄을 빼먹으면 여기서 걸립니다.
"""

from typing import List, Optional, Tuple

Board = List[List[int]]


def find_empty(board: Board) -> Optional[Tuple[int, int]]:
    raise NotImplementedError


def is_valid(board: Board, r: int, c: int, d: int) -> bool:
    raise NotImplementedError


def solve(board: Board) -> bool:
    raise NotImplementedError
