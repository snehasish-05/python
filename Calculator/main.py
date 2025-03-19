from art import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiple(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2



while True:
    print(logo)
    num1 = int(input("Enter the first number "))
    op = input("enter the operator"'\n'
               '+''\n'
               '-''\n'
               '*''\n'
               '/''\n')
    num2 = int(input("Enter the 2nd number " ))
    num_final = 0
    num_n = 0
    num_end = 0

    if op == '+':
        num_final= add(num1,num2)
    elif op == '-':
        num_final = subtract(num1,num2)
    elif op == '*':
        num_final = multiple(num1,num2)
    elif op == '/':
        num_final = divide(num1,num2)

    print(f"{num1} {op} {num2}: {num_final}")
    n = input("Do you want to continue 'y' 'or' 'n' ").lower()
    if n == 'y':
        while True:
            num3 = int(input("Enter the  number "))
            op2 = input("enter the operator"'\n'
                       '+''\n'
                       '-''\n'
                       '*''\n'
                       '/''\n')
            if op2 == '+':
                num_n = add(num_final, num3)
            elif op2 == '-':
                num_n = subtract(num_final, num3)
            elif op2 == '*':
                num_n = multiple(num_final, num3)
            elif op2 == '/':
                num_n = divide(num_final, num3)


            print(f"{num_final} {op2} {num3}: {num_n}")
            n2 = input("Do you want to continue 'y' 'or' 'n' ").lower()
            if n2 == 'y':
                num_final = num_n
            else:
                exit()


    else:
        break








