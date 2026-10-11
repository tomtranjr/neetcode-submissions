class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tkn in tokens:
            if tkn == "+":
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(elem1 + elem2)
            elif tkn == "*":
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(elem1 * elem2)
            elif tkn == "-":
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(elem2 - elem1)
            elif tkn == "/":
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(int(float(elem2) / elem1))
            else:
                stack.append(int(tkn))
        return stack[0]