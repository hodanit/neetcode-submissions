class Solution:
    def isValid(self, s: str) -> bool:
        openBracket = []
        closeBracket = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in closeBracket:
                if openBracket and openBracket[-1] == closeBracket[c]:
                    openBracket.pop()
                else:
                    return False
            else:
                openBracket.append(c)

        return True if not openBracket else False