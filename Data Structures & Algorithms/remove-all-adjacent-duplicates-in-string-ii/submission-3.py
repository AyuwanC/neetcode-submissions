class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        i = 0
        while i < n:
            dup = False
            # print(stack)
            if len(stack) < k:
                stack.append(s[i])
                i += 1
                continue
            else:
                temp = stack[-1]
                for j in range(1,k+1):
                    if stack[-j] != temp:
                        break
                else:
                    dup = True
                if dup:
                    for j in range(k):
                        stack.pop()
                else:
                    stack.append(s[i])
                    i += 1
        if len(stack) >=k:
            temp = stack[-1]
            for j in range(1,k+1):
                if stack[-j] != temp:
                    break
            else:
                dup = True
            if dup:
                for j in range(k):
                    stack.pop()
        return "".join(stack)

        





