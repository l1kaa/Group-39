# 1. https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python
def two_highest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[:2]


# 2. https://www.codewars.com/kata/55f73f66d160f1f1db000059/train/python
def combine_names(first,last):
    return first + " " + last

# 3. https://www.codewars.com/kata/55eca815d0d20962e1000106/train/python
def generate_range(start, stop, step):
    result = []
    while start <= stop:  
        result.append(start)  
        start += step  
    return result

# 4. https://www.codewars.com/kata/55a5befdf16499bffb00007b/train/python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def subt(a, b):
    return a - b

# 5. https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python
def problem(a):
    if type(a) == str:
        return "Error"
    else:
        return (a*50)+6
