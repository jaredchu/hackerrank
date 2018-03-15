def is_matched(expression):
    while len(expression):
        if(expression == middle_out(expression)):
            return False
        expression = middle_out(expression)
    return True

def middle_out(expression):
    brackets = ['[]','{}','()']
    for bracket in brackets:
        expression = expression.replace(bracket,'')
    return expression

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
