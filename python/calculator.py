from math import sin,cos,pi,tan
first_Num = int(input("Enter First Number"))
operator = input("Enter Operator or (Sin,cos,tg,pi) ")
second_Num = int(input("Enter Second Number"))

#Condtion
if operator == "+":
    print(first_Num + second_Num)
elif operator == "-":
    print(first_Num - second_Num)
elif operator == "*":
    print(first_Num * second_Num)
elif operator == "/":
    print(first_Num / second_Num)
elif operator == "sin":
    print(sin(first_Num))
elif operator == "cos":
    print(cos(first_Num))
elif operator == "tan":
    print(tan(first_Num))
elif operator == "pi":
    print(pi)
