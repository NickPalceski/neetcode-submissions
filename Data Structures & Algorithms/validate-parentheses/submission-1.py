class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #key: closing, value: opening
        strMap = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in strMap:
                #stack not empty and top is matched opening
                if stack and stack[-1] == strMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        #Stack empty -> valid
        return True if not stack else False