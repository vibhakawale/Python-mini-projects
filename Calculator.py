import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?:"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation:")
        num2 = float(input("What is the next number?"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue with {answer} or type 'n' to start a new calculation" )

        if choice == "y":
            num1 = answer

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
