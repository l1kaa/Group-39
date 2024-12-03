
#1st task
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
num1 = int(input("please enter a number:"))
num2 = int(input("please enter a number:"))
print(list[num1:num2])

#2nd task
list = ["lika", "nika", "vano", "anka", "sandro"]
num = int(input("please enter an index:"))
print(list[num])

#3rd task
user_name = input("please enter your name:")
name = "lika"
print(user_name[:3] + name[2:])

#4th task
# indexing-ის დროს სიაში ან სტრინგში მოცემულ გარკვეულ ინდექსზე მდგომ ელემენტს ვიძახებთ, ხოლო
# slicing-ის დროს სიიდან ან სტრინგიდან გამოგვაქვს ელემენტები მითითებული დიაპაზონიდან გამომდინარე.

#5th task
surname = input("enter your surname:")
reversed_surname = surname[::-1]
print(surname)
print(reversed_surname)