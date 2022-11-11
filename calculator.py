def add(x, y):
    print(x+y)
    return
def subtract(x, y):
    print(x-y)
    return
def multiply(x, y):
    print(x*y)
    return
def divide(x, y):
    print(x/y)
    return
dictionary_of_operations = {
    "-": subtract,
    "+": add,
    "*": multiply,
    "/": divide
}
list_of_operations = [*dictionary_of_operations.keys()]
string_of_operations = " ".join(list_of_operations)

while True:
    x = int(input("Enter number: " ))
    operation = input(f"Enter operation an operation from the following:  {string_of_operations}")
    y = int(input("Enter number:"))

    if operation == "+":
        add(x,y)
    elif operation == "-":
        subtract(x,y)
    elif operation == "*":
        multiply(x,y)
    elif operation == "/":
        divide(x,y)
    else:
        print("Invalid operation! Please try again...")