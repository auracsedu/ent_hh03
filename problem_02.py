"""
문제 2. 중첩 리스트 세 가지 (함수 3개)

수업 문제 5(flatten)와 같은 중첩 리스트(원소는 정수 또는 리스트, 몇 겹이든 중첩)를
받는 재귀 함수 세 개를 작성하세요. flatten 은 "결과 리스트에 모은다" 하나였지만,
여기서는 숫자를 돌려주는 것, 구조를 유지하는 것, 정보를 하나 더 들고 내려가는 것
세 가지 모양을 익힙니다. 원래 리스트는 어느 함수도 바꾸면 안 됩니다.

max_depth(items)
- 가장 깊이 중첩된 곳의 깊이를 돌려줍니다. 리스트 안에 리스트가 없으면 1 이고,
  빈 리스트도 1 입니다.

deep_reverse(items)
- 모든 층의 리스트를 각각 거꾸로 뒤집은 **새 리스트**를 돌려줍니다. 겉 리스트의
  순서도 뒤집히고, 안쪽 리스트들의 순서도 각각 뒤집힙니다.

flatten_with_depth(items, depth=1)
- flatten 처럼 모든 정수를 원래 순서대로 한 줄로 펼치되, 각 정수가 몇 겹 안에
  있었는지를 함께 (정수, 깊이) 튜플로 돌려줍니다. 겉 리스트에 바로 들어 있는
  정수의 깊이는 1 입니다.
- depth 매개변수는 "지금 이 리스트가 몇 겹째인가"를 재귀로 들고 내려가기 위한
  것입니다. 밖에서 부를 때는 쓰지 않습니다.

예시
    max_depth([1, 2, 3])           -> 1
    max_depth([])                  -> 1
    max_depth([1, [2, 3], 4])      -> 2
    max_depth([[], [[]], []])      -> 3

    deep_reverse([1, 2, 3])            -> [3, 2, 1]
    deep_reverse([1, [2, 3], 4])       -> [4, [3, 2], 1]
    deep_reverse([[1, 2], [3, [4, 5]]]) -> [[[5, 4], 3], [2, 1]]
    deep_reverse([])                   -> []

    flatten_with_depth([1, 2, 3])          -> [(1, 1), (2, 1), (3, 1)]
    flatten_with_depth([1, [2, [3]], 4])   -> [(1, 1), (2, 2), (3, 3), (4, 1)]
    flatten_with_depth([[], [[]], []])     -> []

재귀로 생각하는 법
    세 함수 모두 flatten 과 같이 원소를 하나씩 보고 "정수인가 리스트인가"로 나눕니다.
    리스트면 같은 함수를 다시 부르는데, 돌아온 결과를 어떻게 쓰는가가 다릅니다.

        max_depth:           1 + max_depth(x) 중 가장 큰 값을 고릅니다.
        deep_reverse:        deep_reverse(x) 를 결과에 넣고, 마지막에 결과를 뒤집습니다.
                             (또는 뒤에서부터 돌면서 넣습니다)
        flatten_with_depth:  flatten_with_depth(x, depth + 1) 을 결과에 이어 붙입니다.
                             한 겹 들어갈 때마다 depth 가 1 커집니다.

힌트
    - 어떤 값이 리스트인지 확인: isinstance(x, list)
    - max_depth 는 best = 1 로 시작해 리스트 원소마다 best = max(best, 1 + max_depth(x))
      로 갱신하세요. 리스트 원소가 없으면 best 가 1 로 남아 종료 조건이 저절로 됩니다.
    - deep_reverse 에서 items[::-1] 로 돌면 겉은 뒤집히지만 안쪽 리스트는 그대로입니다.
      안쪽 리스트 자리에는 꼭 deep_reverse(x) 를 넣으세요. 원본을 바꾸지 않아야 하므로
      items.reverse() 는 쓰지 마세요.
    - flatten_with_depth 에서 정수 x 를 넣을 때 깊이는 지금 받은 depth 그대로이고,
      재귀로 들어갈 때만 depth + 1 을 넘깁니다. 튜플은 (x, depth) 로 만듭니다.
"""

from typing import List, Tuple


def max_depth(items: list) -> int:
    raise NotImplementedError


def deep_reverse(items: list) -> list:
    raise NotImplementedError


def flatten_with_depth(items: list, depth: int = 1) -> List[Tuple[int, int]]:
    raise NotImplementedError
