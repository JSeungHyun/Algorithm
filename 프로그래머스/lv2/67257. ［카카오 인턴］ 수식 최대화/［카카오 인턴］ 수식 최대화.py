from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def cal(arr,op):
    exp = arr[:]
    for o in op:
        stack = []
        while len(exp) != 0:
            tmp = exp.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(),exp.pop(0),o))
            else:
                stack.append(tmp)
        exp = stack
    return abs(int(exp[0]))

def solution(expression):
    op = ['+','-','*']
    op = permutations(op,3)
    
    # 기호를 기준으로 split
    exp = [] 
    tmp = ""
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            exp.append(tmp)
            exp.append(i)
            tmp = ""
    exp.append(tmp)
    
    res = []
    for o in op:
        res.append(cal(exp,o))
    return max(res)