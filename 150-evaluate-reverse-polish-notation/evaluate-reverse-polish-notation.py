class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+","-", "*", "/"]
        for elem in tokens:
            if elem not in operator:
                stack.append(int(elem))
            else:
                operandB = stack.pop()
                operandA = stack.pop()
                if elem == "+":
                    res = operandA + operandB
                elif elem == "-":
                    res = operandA - operandB
                elif elem == "*":
                    res = operandA * operandB
                elif elem == "/":
                    res = int(operandA / operandB)
                elif elem =="**":
                    res = operandA ** operandB
                stack.append(res)
        return stack.pop()
                        
                         

        