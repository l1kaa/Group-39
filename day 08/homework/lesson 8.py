# task 1
#მეტობა 
5>2, 303>104, 45555>405

#ნაკლებობა 
134<2009, 7<177, 5463<5688

#მეტია ან ტოლია
40>=39, 56>=56, 308>=90

#ნაკლებია ან ტოლია 
309<=309, 988<=1002, 7899<=7899

# task 2
fav_number = 4
users_number = int(input("please enter your favourite number:"))
print(fav_number==users_number)

# task 3
print(True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5)
# True or False (True)
# 5 > 3 (True)
# "name" == "name" (True)
# 123 == "123" (False)
# 5 >= 5 (True)
# ეს კოდი გამოიტანს True-ს რადგან ჯდება შემდეგი თანმიმდევრობით:
#True and True or True and False and True (result: True)

# task 4
my_surname = "chxikvadze"
users_age = int(input("please enter your age:"))
users_surname = input("please enter your surname:")
print (users_age >= 18 or users_surname == my_surname)

# task 5
# ალგორითმი არის გარკვეული დავალების შესასრულებლად საჭირო მოქმედებათა ზუსტი თანმიმდევრობა.
# An algorithm is a set of step-by-step instructions to accomplish a task or solve a problem,placed in a certain order.
# ალგორითმის მაგალითები რეალურ ცხოვრებაში: 1.გაკვეთილების ცხრილი 2.დღის განრიგი 3.საჭმლის მომზადების რეცეპტი

# task 6
# Flowchart - ხელს უწყობს ალგორითმების ვიზუალიზაციას.
# pseudocode - არის ალგორითმის გამოსახვა, რომელიც იყენებს როგორც ნატურალურ ენას, ასევე პროგრამირების ელემენტებს.

# task 7
# Sequencing ნიშნავს რომ ჩვენი კოდი თანმიმდევრობით ზემოდან ქვემოთ გაეშვება.
# Iteration არის ინსტრუქციის განმეორებით შესრულება.
# Selection განსაზღვრავს გარკვეულ არჩევანს.

# task 8
num1 = int(input("please choose any number: "))
num2 = int(input("please choose any number for the second time: "))
num3 = int(input("please choose any number for the third time:  "))
num4 = int(input("please choose any number for the fourth time: "))
num5 = int(input("please choose any number for the fifth time: "))

arithmetic_mean = (num1 + num2 + num3 + num4 +num5)/53
print(arithmetic_mean < num1*num5)


