# 1. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ string-ს, შემდეგ შეაერთეთ ისინი და დაპრინტეთ.
def concatinate(string1, string2):
    return string1 + string2
print(concatinate)

# 2. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ 5 ელემენტიან რიცხვების სიას, შემდეგ დაპრინტეთ სიის მე-3 ელემენტისა და მე-4 ელემენტის ჯამი.
def list(numbers):
    return numbers[2] + numbers[3]
print(list)

# 3. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ მანძილს კილომეტრში, შემდეგ გადააქციეთ ის მეტრში და დაპრინტეთ.
def convert(km):
    return km / 1000
print(convert)

# 4. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ რიცხვს, შემდეგ დაპრინეთ ამ ორი რიცხვიდან უფრო დიდი.
def max(num1,num2):
    if num1>num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "the numbers are equal", num1,num2

# 5. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ სტრინგს, შემდეგ შეაბრუნეთ ეს სტრინგი და დაპრინტეთ.
def reverse(string):
    return string[::-1]
print(reverse)

