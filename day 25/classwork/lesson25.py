# 1)შექმენით სია, სადაც დაამატებთ 5 ელემენტს, შემდეგ კი გამოიტანე მესამე და მეოთხე ელემენტები.
list3 = ["computer", "headphones", "keyboard", "mouse pad", "mouse"]
print(list3[2:4])

# 2)შექმენით სია, სადაც დაამატებთ 5 ელემენტს, შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და რომელ რიცხსაც შემოიტანთ მისი ინდექსი დაპრინტეთ
list3 = ["computer", "headphones", "keyboard", "mouse pad", "mouse"]
index = int(input("enter a number from 0 to 4:"))
if index <= 4 or 4 <= index <=-5:
    print(list3[index])
else:
    print("invalid answer. try again.")