class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in closeToOpen:
                if myStack and myStack[-1] == closeToOpen[c]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(c)
        return True if not myStack else False

            