import operator
import re

def parse_token(token):
    # ???
    return token

OPERATOR_TO_LAMBDA = {
}
 
def execute(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    for op in OPERATORS.keys():
        expr = expr.replace(op, ' ' + op + ' ')
    expr = re.sub(' +',' ', expr)
    expr = expr.strip(' ')
    index = 0
    
    #calculate
    stack = [0]
    for token in expr.split(" "):
        try:
            if token in OPERATORS:
                op2, op1 = stack.pop(), stack.pop()
                if '.' in op1 or '.' in op2:
                    op1, op2 = float(op1), float(op2)
                    stack.append(str(OPERATORS[token](op1,op2)))
                else:                
                    op1, op2 = int(op1), int(op2)
                    stack.append(str(int(OPERATORS[token](op1,op2))))
            elif token:
                stack.append(token)
        except:
            raise ValueError('Incorrect Reverse Polish Notation \n' + expr + '\n' + ' ' * (2 * index) + '^')
        index += 1
    res = stack.pop()
    return float(res) if '.' in res else int(res)
