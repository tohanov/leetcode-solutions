class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        closing_brackets = {
            "[": "]",
            "(": ")",
            "{": "}",
        }

        for bracket in s:
            if bracket in closing_brackets.keys():
                stack.append(closing_brackets[bracket])
            elif len(stack) != 0 and bracket == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
