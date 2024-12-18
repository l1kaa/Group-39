# 1)მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ შეეკითხეთ როგორ უნდა სახელის შეცვლა (lower/upper/capitalize) თუ შემოიტანს upper, მაშინ დაუბეჭდეთ სახელი გადიდებულად, თუ შემოიტანს lower, მაშინ დაუბეჭდეთ სახელი დაპატარავებულად და თუ შემოიტანს capitalize, მაშინ სახელის პირველი ასო გაუდიდეთ.

user_surname = input("enter your surname: ")
change_to = input("how do you want to change your surname? , choose 1)upper; 2)lower; or 3)capitalize: ")
change_to = change_to.lower()

if change_to == "upper":
    print(user_surname.upper())
elif change_to == "lower":
    print(user_surname.upper())
elif change_to == "capitalize":
    print(user_surname.capitalize())
while change_to != "upper" "lower" "capitalize":
    change_to = input("please enter a valid answer:")


# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ თუ გვარი შეიცავს სიმბოლოებს "shvili" მაშინ დაუბეჭდეთ "როგორ ხარ?" თუ შეიცავლს "ia" მაშინ დაუბეჭდეთ "მუჭო რექ?" სხვა შემთხვევაში "Bye".

surname = input("enter a surname: ")
if surname.find("shvili") > 0:
    print("როგორ ხარ?")
elif surname.find("ia") > 0:
    print("მუჭო რექ?")
else:
    print("bye")


# 3)შექმენით სახელების სია, შემდეგ მომხმარებელს შემოატანინეთ სახელი და თუ სახელის იწყება ასო "d"-თი და ბოლოვდება ასო "i"-თ, მაშინ დაამატეთ სახელების სიაში, სხვა შემთხვევაში დაუბეჭდეთ "invalid".

names = ["lika", "nika", "vano"]
user_name = input("enter a name: ")
if user_name.find(0) == "d" and user_name.find(0) == "i":
    names.append(user_name)
    print(names)
else:
    print("invalid")


# 4)შექმენით 10 ელემენტიანი სია, შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და ამოაგდეთ ამ რიცხვის ინდექსზე მდგომი ელემენტი სიიდან, ბოლოს დაბეჭდეთ სია.

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
character = int(input("enter an index: "))
list.pop(character)
print(list)


# 5)შექმენით 5 ელემენტიანი სია, მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ მისი საყვარელი საჭმელი, შემდეგ ამ შემოტანილი რიცხვის ინდექსზე დაამატეთ მისი საყვარელი საჭმელი და დაბეჭდეთ სია.

food = ["cake", "banana", "apple", "cupcake", "pasta"]
num = int(input("enter a number: "))
fav_food = input("enter your favorite food: ")
food.insert(num,food)
print(food)