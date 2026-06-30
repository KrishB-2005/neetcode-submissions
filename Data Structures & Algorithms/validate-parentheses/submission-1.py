class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        h = { ")" : "(", "]":"[", "}" : "{"}

        for i in s:
            if i in h:
                if stack and stack[-1] == h[i]:

                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False