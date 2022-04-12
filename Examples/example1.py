#1 Simple Calculator Using functions
def Calculator(a,b,c):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        return a/b
    else:
        return "Invalid operator"
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator: ')
print(Calculator(num1,num2,op))
