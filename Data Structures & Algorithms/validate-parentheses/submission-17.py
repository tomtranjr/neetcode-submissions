class Solution:
    def isValid(self, s: str) -> bool:
        # brute force
        # while any of parenthesis in string, replace it
        # check if string is empty
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""

        # stack
        # init stack and create dict (close: open)
        # iter through s
        # if opening, add to stack
        # we are on closing, verify that the parenthesis at top of stack is the opening using dict
        # if not match, return False
        # otherwise, it is match, we pop from stack and continue
        stack = []
        closeToOpen = {"}": "{", ")": "(", "]": "["}

        for char in s:
            if char in closeToOpen.values():
                stack.append(char)
            if stack and char != stack[-1]:
                return False
            stack.pop()
        
        return stack