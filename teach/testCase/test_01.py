import pytest


def add_func(x):
    return x+1

def test_01():
    print('用例1开始')
    assert add_func(1) == 2
    print('用例1结束')

def test_02():
    assert add_func(2) == 3


if __name__ == '__main__':
    pytest.main(['-s'])