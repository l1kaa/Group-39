# 1st task: https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python
def calculator(x,y,op):
    if type(x) == int and type(y) == int:
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
    else:
        return "unknown value"
    return "unknown value"
# 2nd task: შექმნით სია 5 ელემენტით, შემდეგ კი დაპრინტეთ ამ ელემენტების ჯამი, for loop.
list = [700,450,67,13,56]
count = 0
for i in list:
    count+= i
print(count)