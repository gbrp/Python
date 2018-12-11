x = int(raw_input("Enter the value for x: "))
print x

y = int(raw_input("Enter the value for y: "))
print y

operation = raw_input("Choose mart operation (+, -, *, /: ")
print operation

if operation == "+":
    print x+y
elif operation == "-":
    print x - y
elif operation == "*":
    print x * y
elif operation == "/":
    print x / y
else:
    print ("You didn't provide the correct math operation")
