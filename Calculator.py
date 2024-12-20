import art
def whole():
    print(art.logo)
    print("welcome to a simple calculator\n")
    num1 = int(input("Please enter the first number : "))
    stop = True
    while  stop:
        num2 = int(input(f"Please enter the second number : "))
        operation=str(input("Choose one of the operations :"
                         "list of operations are :\n"
                         "+\n"
                         "-\n"
                         "*\n"
                         "/\n"
                         f"You picked  : "))


        def calculator(x,y):
            def add(n1, n2):
                return n1 + n2
            def subtract(n1,n2):
                return n1-n2
            def multiply(n1,n2):
                return n1*n2
            def divide(n1,n2):
                return n1/n2
            if operation== '+':
                return add(x,y)
            elif operation== '-':
                return subtract(x,y)
            elif operation== '*':
                return multiply(x,y)
            elif operation== '/':
                return divide(x,y)
            else:
                return "Invalid input"

        result= calculator(num1,num2)
        if result=="Invalid input":
            print("Invalid input")
        else:
            print(f"The Result of {num1} {operation} {num2} = {result}")
        choice = str(input(f"Type yes if would you like to continue using the current value {result} or  no if you want to strat a new calculation\n"
                  f"Yes for continue with current value | No  for starting a new calculation : "))
        if choice.lower()=='yes':
            num1=result

        elif choice.lower()=='no':
            stop=False
            print("\n" * 100)
            whole()
        else :
            print("Invalid input")

whole()
