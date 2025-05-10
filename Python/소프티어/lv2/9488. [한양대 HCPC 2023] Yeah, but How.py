import sys
input = sys.stdin.readline

result = ''
parentheses = input().rstrip()

""" 
for p in parentheses:
    if p == '(':
        result += '('
    else:
        result += '1)'
        

result = result.replace(')1', ')+1').replace(')(', ')+(')
print(result) 
"""

print(parentheses.replace("()", "(1)").replace(")(", ")+("))
