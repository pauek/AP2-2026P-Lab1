from typing import Any
from polish import evaluate, main
import pytest
import io


def test_evaluate_one():
    assert evaluate("99") == 99


def test_evaluate_sum():
    assert evaluate("3 154 +") == 157


def test_evaluate_sub():
    assert evaluate("3 2 -") == 1


def test_evaluate_complex():
    assert evaluate("3 4 + 2 8 - * 2 5 + +") == -35


def test_evaluate_empty():
    with pytest.raises(Exception):
        evaluate("")


def test_evaluate_wrong_1():
    with pytest.raises(Exception):
        evaluate("5 4 2 3 +")


def test_evaluate_wrong_2():
    with pytest.raises(Exception):
        evaluate("1 2 3 + + + +")


def test_evaluate_wrong_operator():
    with pytest.raises(Exception):
        evaluate("5 4 $")


def main_tester(testcase: str, monkeypatch: Any):
    inp_file = testcase + ".inp"
    cor_file = testcase + ".cor"
    out_file = io.StringIO()
    monkeypatch.setattr("sys.stdin", io.StringIO(open(inp_file).read()))
    monkeypatch.setattr("sys.stdout", out_file)
    main()
    assert out_file.getvalue() == open(cor_file).read()


def test_main_sample1(monkeypatch: Any):
    main_tester("01-polish/sample1", monkeypatch)


def test_main_sample2(monkeypatch: Any):
    main_tester("01-polish/sample2", monkeypatch)
