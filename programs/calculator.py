from art import logo
def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

    
def calculator ():
    should_continue = True
    print(logo)
    num1 = float(input("enter a number: "))
    while should_continue:
        
        operator = input("enter the operator")
        num2 = float(input("enter the next number: "))
        calc = operators[operator]
        answer = calc(num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
        if input(f"type 'y' to continue with {answer} or 'n' to start a new calculation") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

   
    

    






