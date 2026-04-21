class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operaters = ['+' , '-', '*', '/']
        stack = deque()
        for token in tokens:
            if token not in operaters:
                stack.append(token)
                print(stack)
            else:
                pop = stack.pop()
                pop2 = stack.pop()
                operation = str(pop2) + token + str(pop)
       
                stack.append(int(eval(operation)))
                print(stack)
        return int(stack[-1])


        