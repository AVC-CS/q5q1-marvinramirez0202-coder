import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # Input: 3 -> rows: A / A B / A B C
    content = open('result1.txt').read()
    print(content)
    regex_test([r'(?m)^A\s*$', r'(?m)^A B\s*$', r'(?m)^A B C\s*$'], content)


@pytest.mark.T2
def test_main_2():
    # Input: 5 -> rows: A / A B / A B C / A B C D / A B C D E
    content = open('result2.txt').read()
    print(content)
    regex_test([r'(?m)^A\s*$', r'(?m)^A B C\s*$', r'(?m)^A B C D E\s*$'], content)


@pytest.mark.T3
def test_main_3():
    # Input: 4 -> rows: A / A B / A B C / A B C D
    content = open('result3.txt').read()
    print(content)
    regex_test([r'(?m)^A\s*$', r'(?m)^A B C\s*$', r'(?m)^A B C D\s*$'], content)


@pytest.mark.T4
def test_main_4():
    # Input: 6 -> rows: A / A B / ... / A B C D E F
    content = open('result4.txt').read()
    print(content)
    regex_test([r'(?m)^A\s*$', r'(?m)^A B C D\s*$', r'(?m)^A B C D E F\s*$'], content)
