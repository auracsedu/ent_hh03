"""
문제 3. 고르는 재귀 (함수 2개)

수업 문제 7(combinations)의 "쓴다 / 안 쓴다"를 두 가지로 변형합니다. 하나는 같은
것을 여러 번 쓸 수 있고 가짓수만 세며, 하나는 만들어 가는 중간 상태를 인자로 들고
내려갑니다.

count_change(amount, coins)
- 동전 종류 리스트 coins 로 amount 원을 만드는 방법의 수를 돌려줍니다.
- 각 동전은 몇 개든 쓸 수 있습니다.
- 순서는 구별하지 않습니다. 1+2 와 2+1 은 같은 방법입니다.
- amount 가 0 이면 "아무것도 안 쓰는" 한 가지 방법이 있으므로 1 입니다.
- coins 는 서로 다른 양의 정수이고 비어 있을 수 있습니다. amount 는 0 이상입니다.

generate_parentheses(n)
- 여는 괄호 "(" 와 닫는 괄호 ")" 를 n 개씩 써서 만들 수 있는 올바른 괄호 문자열을
  모두 담은 리스트를 돌려줍니다.
- 올바른 괄호 문자열: 왼쪽에서 읽어 갈 때 닫는 괄호가 여는 괄호보다 많아지는 순간이
  없고, 끝에서 둘의 개수가 같습니다.
- 순서는 "같은 자리에서는 ( 를 먼저 시도한 것"이 먼저입니다. (아래 예시의 순서)
- n 이 0 이면 [""] 입니다.

예시
    count_change(0, [1, 2])         -> 1
    count_change(4, [1, 2])         -> 3        # 1+1+1+1, 1+1+2, 2+2
    count_change(5, [1, 2, 5])      -> 4        # 1*5, 1*3+2, 1+2+2, 5
    count_change(3, [2])            -> 0
    count_change(3, [])             -> 0
    count_change(100, [1, 5, 10, 25, 50]) -> 292

    generate_parentheses(0) -> [""]
    generate_parentheses(1) -> ["()"]
    generate_parentheses(2) -> ["(())", "()()"]
    generate_parentheses(3) -> ["((()))", "(()())", "(())()", "()(())", "()()()"]

재귀로 생각하는 법
    count_change: 맨 앞 동전 coins[0] 을 보고 두 경우로 나눕니다.

        쓴다   -> amount - coins[0] 을 **같은 coins 로** 만드는 방법 수
                  (같은 동전을 또 쓸 수 있으니 coins 를 줄이지 않습니다)
        안 쓴다 -> amount 를 coins[1:] 로 만드는 방법 수
                  (이 동전은 이제 영원히 안 씁니다)

        두 수를 더하면 답입니다. 종료 조건은 amount == 0 이면 1,
        amount < 0 이거나 coins 가 비었으면 0 입니다.
        수업 문제 7 과 비교해 보세요. "쓴다" 쪽에서 리스트가 줄어들지 않는 것이
        유일한 차이이고, 그래서 같은 동전을 여러 번 쓸 수 있게 됩니다.

    generate_parentheses: 지금까지 만든 문자열 cur, 쓴 여는 괄호 수 open, 쓴 닫는
    괄호 수 close 를 들고 내려가는 재귀 함수 go(cur, open, close) 를 만듭니다.

        1) 문자열 길이가 2n 이면 완성입니다. 결과에 넣습니다.
        2) open < n 이면 "(" 를 붙여서 go 를 부릅니다.
        3) close < open 이면 ")" 를 붙여서 go 를 부릅니다.

        2) 를 3) 보다 먼저 하면 요구한 순서가 저절로 나옵니다. close < open 조건이
        "닫는 괄호가 많아지는 순간이 없다"를 보장합니다.

힌트
    - count_change(4, [1, 2]) 를 종이에 트리로 그려 보면 왜 3 인지 보입니다.
    - go 는 결과 리스트 result 에 append 만 하고 아무것도 돌려주지 않아도 됩니다.
      result 는 generate_parentheses 안에서 만들고 마지막에 돌려주세요.
    - n 이 0 이면 길이 0 인 cur = "" 가 바로 완성 조건에 걸려 [""] 가 나옵니다.
      따로 처리하지 않아도 됩니다.
"""

from typing import List


def count_change(amount: int, coins: List[int]) -> int:
    raise NotImplementedError


def generate_parentheses(n: int) -> List[str]:
    raise NotImplementedError
