num1 = float(input("insert your 1st number: "))
oper = input("insert your operatorr: ")
num2 = float(input("insert your 2nd number: "))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "*":
    print(num1 * num2)
else:
    print("not a valid operator")