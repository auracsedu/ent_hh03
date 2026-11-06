import pytest

from problem_01 import my_int, tokenize, with_commas


@pytest.mark.parametrize(
    "s, expected",
    [
        ("0", 0),
        ("42", 42),
        ("  -15 ", -15),
        ("+007", 7),
        ("-0", 0),
        ("1234567", 1234567),
        ("   8", 8),
        ("9   ", 9),
        ("-1000", -1000),
    ],
)
def test_my_int(s, expected):
    assert my_int(s) == expected
    assert type(my_int(s)) is int


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (7, "7"),
        (999, "999"),
        (1000, "1,000"),
        (12345, "12,345"),
        (1234567, "1,234,567"),
        (-1234, "-1,234"),
        (-999, "-999"),
        (100000, "100,000"),
        (1000000000, "1,000,000,000"),
    ],
)
def test_with_commas(n, expected):
    assert with_commas(n) == expected


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("1+2", ["1", "+", "2"]),
        ("12+ 3*(45-6)", ["12", "+", "3", "*", "(", "45", "-", "6", ")"]),
        ("  7  ", ["7"]),
        ("((1))", ["(", "(", "1", ")", ")"]),
        ("", []),
        ("   ", []),
        ("10 20", ["10", "20"]),
        ("100/25-3", ["100", "/", "25", "-", "3"]),
        ("-5", ["-", "5"]),
        ("2*(3+4)*5", ["2", "*", "(", "3", "+", "4", ")", "*", "5"]),
    ],
)
def test_tokenize(expr, expected):
    assert tokenize(expr) == expected
