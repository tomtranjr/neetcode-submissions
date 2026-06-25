class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        characters = {')':'(', '}':'{', ']':'['}

        # for char in s:
        #     if char in characters.values():
        #         stack.append(char)
        #     if characters[char] != stack[-1]:
        #         return False
        #     else:
        #         stack.pop()
        # return True
        for c in s:
            if c in characters:
                if stack and stack[-1] == characters[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False