class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        out = 0
        print(5 / 13)
        print((5 / 13) + 4)
        for t in tokens:
            if t == "+":
                temp = int(stack[-1])
                stack.pop()
                temp = int(stack[-1]) + temp
                stack.pop()
                stack.append(temp)
            elif t == "*":
                temp = int(stack[-1])
                stack.pop()
                temp = int(stack[-1]) * temp
                stack.pop()
                stack.append(temp)
            elif t == "-":
                temp = int(stack[-1])
                stack.pop()
                temp = int(stack[-1]) - temp
                stack.pop()
                stack.append(temp)
            elif t == "/":
                temp = int(stack[-1])
                stack.pop()
                temp = int(stack[-1]) / temp
                stack.pop()
                stack.append(temp)
            else:
                stack.append(t)
        
        return int(stack[0])
