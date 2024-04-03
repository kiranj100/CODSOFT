# Using Decorator
def outer_function(number):
    def inner_function():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return number(num1, num2)

    return inner_function


@outer_function
def Addition(a, b):
    return a + b


@outer_function
def Subtraction(a, b):
    return a - b


@outer_function
def Multiplication(a, b):
    return a * b


@outer_function
def Division(a, b):
    if b == 0:
        return "Error: You Can't Divide by zero!"
    else:
        return a / b


print("Select Operations:")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

select_number = input("Enter One Operation You Want to Perform:")

if select_number in ('1', '2', '3', '4'):
    if select_number == '1':

        print("Result:", Addition())
    elif select_number == '2':
        print("Result:", Subtraction())
    elif select_number == '3':
        print("Result:", Multiplication())
    elif select_number == '4':
        print("Result:", Division())
else:
    print("Please Enter Valid Value")
