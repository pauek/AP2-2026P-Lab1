import sys


def evaluate(expression: str) -> int:
    stack = list[int]()
    for word in expression.split():
        if word.isdigit():
            stack.append(int(word))
        else:
            assert len(stack) >= 2, "Not enough operands"
            p1 = stack.pop()
            p2 = stack.pop()
            if word == "+":
                stack.append(p1 + p2)
            elif word == "-":
                stack.append(p2 - p1)
            elif word == "*":
                stack.append(p1 * p2)
            else:
                assert False, "Unknown operator"
    assert len(stack) == 1, "Syntax error"
    return stack[0]


def main() -> None:
    for expression in sys.stdin:
        print(evaluate(expression))


if __name__ == "__main__":  # pragma: no cover
    main()
