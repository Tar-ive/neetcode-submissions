class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack= []
        for operation in operations: 
            if operation == "+":
                if len(stack) >=2:
                    operator1= stack[-1]
                    operator2= stack[-2]
                    sum_= operator1+operator2
                    stack.append(sum_)
            elif operation == "D":
                if stack:
                    prev = stack[-1]
                    stack.append(prev * 2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)   