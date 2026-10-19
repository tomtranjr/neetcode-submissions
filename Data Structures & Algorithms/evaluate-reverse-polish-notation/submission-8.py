class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tkn in tokens:
            if tkn == "+":
                elem = stack.pop(-2) + stack.pop(-1)
                stack.append(elem)
            elif tkn == "-":
                elem = stack.pop(-2) - stack.pop(-1)
                stack.append(elem)
            elif tkn == "*":
                elem = stack.pop(-2) * stack.pop(-1)
                stack.append(elem)
            elif tkn == "/":
                elem = float(stack.pop(-2)) / stack.pop(-1)
                stack.append(int(elem))
            else:
                stack.append(int(tkn))
        
        return stack[0]