class Solution:
    def isValid(self, s: str) -> bool:
        # can put pair of parentheses on the stack 
        # then use a stack. 
        # given a closing parenthesis, check if open is in the top of stack, if yes pop, if no return False immediately. 

        stack = []
        hash = {}
        hash["}"] = "{"
        hash["]"] = "["
        hash[")"] = "("

        #insert into stack 
        for p in s: 
            if p == "{" or p == "[" or p == "(": 
                stack.append(p)
            elif len(stack) !=0 and stack[-1] == hash[p]: 
                stack.pop()
            else: 
                return False
                     # trying to check if given a string, its value is in hash or not. 
                     # i am pushing and popping the wrong thing. also i dont know if it can be 1 operation or is multiple operations. 
                # i need to push non ] things in stack? 
        print(stack)
        return len(stack) == 0 

