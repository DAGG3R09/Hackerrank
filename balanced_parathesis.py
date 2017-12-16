starts = ["(","{","["]
ends = {
        ")": "(",
        "}": "{",
        "]": "[",
}

def isBalanced(S):
    stack = []
    for s in S:
        if s in starts:
            stack.append(s)
        elif s in ends:
            if len(stack) == 0 or stack[-1] != ends[s]:
                return ("NO")
            else:
                stack.pop()

    if len(stack) == 0:
        return ("YES")
    else:
        return("NO")



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
