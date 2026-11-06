"""
문제 4. N-퀸 (함수 3개)

n x n 체스판에 퀸 n 개를 서로 공격하지 못하게 놓는 문제입니다. 퀸은 같은 행, 같은
열, 같은 대각선에 있는 말을 공격합니다. 한 행에 퀸을 하나씩 놓으므로, 놓은 자리는
"r 번째 행의 퀸이 있는 열 번호"를 담은 리스트 cols 로 나타냅니다. cols = [1, 3, 0, 2]
는 0행 1열, 1행 3열, 2행 0열, 3행 2열에 퀸이 있다는 뜻입니다.

is_safe(cols, c)
- 지금까지 0행부터 len(cols) - 1 행까지 놓았을 때, 다음 행(len(cols) 행)의 c 열에
  퀸을 놓아도 되는지 돌려줍니다. 이미 놓인 퀸 중 하나라도 같은 열이거나 같은
  대각선에 있으면 False 입니다.

solve_n_queens(n)
- 가능한 배치를 모두 담은 리스트를 돌려줍니다. 각 배치는 길이 n 인 cols 리스트입니다.
- 배치들의 순서는 "앞 행의 열 번호가 작은 것"이 먼저입니다. (각 행에서 열을 0 부터
  차례로 시도하면 저절로 그렇게 됩니다.)
- 배치가 없으면 [] 입니다. n 은 1 이상입니다.

count_n_queens(n)
- 가능한 배치의 개수를 돌려줍니다.

예시
    is_safe([], 0)          -> True
    is_safe([0], 0)         -> False    # 같은 열
    is_safe([0], 1)         -> False    # 바로 아래 오른쪽 대각선
    is_safe([0], 2)         -> True
    is_safe([1, 3], 0)      -> True
    is_safe([1, 3], 2)      -> False    # 1행 3열 퀸과 대각선

    solve_n_queens(1)   -> [[0]]
    solve_n_queens(2)   -> []
    solve_n_queens(3)   -> []
    solve_n_queens(4)   -> [[1, 3, 0, 2], [2, 0, 3, 1]]
    count_n_queens(6)   -> 4
    count_n_queens(8)   -> 92

재귀로 생각하는 법
    수업 문제 8(permutations)과 extra 2(백트래킹)를 합친 모양입니다.

        go(cols) = "cols 까지 놓은 상태에서 나머지 행을 모두 채우는 방법을 전부 찾아
                    result 에 넣는다"

        1) len(cols) == n 이면 완성입니다. cols 의 **복사본**을 result 에 넣습니다.
        2) 아니면 c 를 0 부터 n-1 까지 돌면서 is_safe(cols, c) 인 c 마다
               cols.append(c)   ->   go(cols)   ->   cols.pop()
           을 합니다. append 와 pop 이 짝이라는 것이 백트래킹의 전부입니다.

힌트
    - 대각선 판정: 놓인 퀸이 r 행 cols[r] 열에 있고 새 퀸이 len(cols) 행 c 열이면,
      행 차이와 열 차이의 절댓값이 같을 때 대각선입니다.
      abs(cols[r] - c) == len(cols) - r
    - 1) 에서 복사본을 넣지 않고 result.append(cols) 라고 쓰면, 그 뒤의 pop 이 result
      안에 들어간 리스트까지 비워 버려 결과가 전부 [] 가 됩니다. cols[:] 또는
      list(cols) 를 넣으세요. (가변 객체가 공유된다는 2주차 내용입니다)
    - count_n_queens 는 len(solve_n_queens(n)) 으로 끝낼 수 있습니다. 한 줄이면 됩니다.
    - n = 8 일 때 시도하는 자리는 수천 개 정도라 1초 안에 끝납니다. 끝나지 않으면
      is_safe 가 틀린 자리를 통과시키고 있거나 pop 이 빠진 것입니다.
"""

from typing import List


def is_safe(cols: List[int], c: int) -> bool:
    raise NotImplementedError


def solve_n_queens(n: int) -> List[List[int]]:
    raise NotImplementedError


def count_n_queens(n: int) -> int:
    raise NotImplementedError
