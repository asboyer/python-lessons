first = input("First number: ")
operation = input("Operation: ")
second = input("Second number: ")
if operation == "x":
    final = float(first) * float(second)
elif operation == "^":
    final = float(first) ** float(second)
else:
    final = eval(first + operation + second)
print(final)
