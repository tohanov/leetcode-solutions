class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        operations = {
            "-": lambda a, b: a - b,
            "+": lambda a, b: a + b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }

        for token in tokens:
            if token in operations:
                b = stack.pop()
                stack.append(operations[token](stack.pop(), b))
            else:
                stack.append(int(token))

        return stack[0]
