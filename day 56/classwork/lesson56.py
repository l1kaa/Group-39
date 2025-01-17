# 1. https://www.codewars.com/kata/524f5125ad9c12894e00003f
def remainder(a,b):
    if a > b:
        if b == 0:
            return None
        else:
            return a % b
    elif b > a:
        if a == 0:
            return None
        else:
            return b % a
    elif a < 0 and b < 0:
        return 0


# 2. https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 3. https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
def is_uppercase(inp):
    if inp == inp.upper() or inp == " ":
        return True
    else:
        return False
