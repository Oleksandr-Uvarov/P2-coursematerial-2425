import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize("string", [
    "",
    "()",
    "(())",
    "()()",
    "((()))"
])
def test_true_matching_parentheses(string):
    assert matching_parentheses(string) == True

@pytest.mark.parametrize("string", [
    ")",
    ")()",
    ")(",
    ")()(",
    ")(())("
])
def test_false_matching_parentheses(string):
    assert matching_parentheses(string) == False