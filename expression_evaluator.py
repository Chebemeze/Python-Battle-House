def evaluate(expression):
    # TODO: parse and evaluate the arithmetic expression yourself, respecting
    # operator precedence and parentheses. Do not use eval() or exec().
    
    #steps:
    #1 strip away inside spaces first
    #check if operator exist by calling operator checker function
    # perform the actual calculation using calc_function(). It takes
    # in the sign and two operand to perform the calculation. Inside this function it check
    # if "*" multiplies the two numbers. if "+" adds the two numbers. If "-" subrtract
    #number two from first number
    
    # improving this would require looking for parenthesis first. 
    # This will tell us where to begin overall calculation from.

    expression = expression.replace(" ", "")
    # print(expression)
    values = []
    operators = []
    def perform_operations():
        right = values.pop()
        left = values.pop()
        operator = operators.pop()
        operations = {
            "*": left*right,
            "+": left+right,
            "/": left/right,
            "-": left-right
        }
        res = operations[operator]
        values.append(res)
            
    precedence_order = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10  + int(expression[i])
                i+= 1
            values.append(float(num))
            continue
   
        elif char == "(":
            operators.append(char)
        elif char == ")":
            while operators[-1] != "(":
                perform_operations()
            operators.pop()
        elif char in "*/+-":
            if operators and precedence_order[operators[-1]] >= precedence_order[char]:
                perform_operations()
            operators.append(char)
        i+=1
    while operators:
        perform_operations()
    return values[0]

print(evaluate("20 + 3*4"))
#32
print(evaluate("2+3"))
# #5.0
print(evaluate("2+3* 4"))
# #14.0 (multiplication first)
print(evaluate("(2+3)*4"))
# #20.0 (parentheses first)
print(evaluate("(100+1)"))
#101.0
print(evaluate("2*(3+4)-5"))
#9