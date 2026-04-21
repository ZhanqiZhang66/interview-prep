class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operaters = ['+' , '-', '*', '/']
        stack = deque()
        for token in tokens:
            if token not in operaters:
                stack.append(token)
            else:
                pop = stack.pop()
                pop2 = stack.pop()
                operation = str(pop) + token + str(pop2)
                print(stack)
                stack.append(int(eval(operation)))
        return int(stack[-1])


        