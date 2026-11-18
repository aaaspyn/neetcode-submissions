class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchD = {")":"(", "]":"[", "}": "{"}

        for c in s:
            if c in matchD: 
                if stack and stack[-1] == matchD[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
            