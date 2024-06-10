#Basic Calculator

Num1 = int(input("Enter 1st number: "))
Ope = (input("Enter a operator: "))
Num2 = int(input("Enter a 2nd number: "))
oper1 = "+"
oper2 = "-"
oper3 = "/"
oper4 = "*"

if Ope == oper1:
  temp = Num1 + Num2
  print(f"Your answer will be {temp}")

elif Ope == oper2:
  temp = Num1 - Num2
  print(f"Your answer will be {temp}")

elif Ope == oper3:
  temp = Num1 / Num2
  print(f"Your answer will be {temp}")

elif Ope == oper4:
  temp = Num1 * Num2
  print(f"Your answer will be {temp}")

else:
  print("Please put a correct operator")