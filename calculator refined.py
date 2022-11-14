def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    result = 0
    for i in range(y):
        result = add(result, x)
    return result
def divide(x, y):
    return x/y
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
    y = int(input("Enter number: "))

    if operation == "+":
        print(add(x,y))
    elif operation == "-":
        print(subtract(x,y))
    elif operation == "*":
        print(multiply(x,y))
    elif operation == "/":
        print(divide(x,y))
    else:
        print("Invalid operation! Please try again...")