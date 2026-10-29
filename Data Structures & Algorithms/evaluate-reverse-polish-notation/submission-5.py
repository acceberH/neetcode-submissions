class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    result = b + a
                elif token == '-':
                    result = b - a
                elif token == '*':
                    result = b * a
                elif token == '/':
                    result = int(b / a)

                stack.append(result)
        return stack[-1]

        