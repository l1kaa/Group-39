# 1. https://www.codewars.com/kata/523b4ff7adca849afe000035
def greet():
    return "hello world!"

# 2. https://www.codewars.com/kata/56200d610758762fb0000002
def add_five(num):
    num = num + 5
    return num

# 3. https://www.codewars.com/kata/55685cd7ad70877c23000102
def make_negative( num ):
    if num > 0:
        return num * -1
    elif num == 0:
        return 0
    else:
        return num

# 4. https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

# 5. https://www.codewars.com/kata/57089707fe2d01529f00024a
def check_alive(health):
    if health <= 0:
        return False
    else:
        return True 
