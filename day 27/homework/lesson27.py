# 1. კომენტარების მეშვეობით ახსენი რა არის .upper().
# .upper() --> სტრინგი გადაჰყავს upper case-ში


# 2. კომენტარების მეშვეობით ახსენი რა არის .lower()
# .lower() --> სტრინგი გადაჰყავს lower case-ში


# 3. ცვლადში შეინახე სტრინგი დიდი ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ, დააკვირდი რა მოუვათ სხვა ასოებს.
group = "GROUP 39"
group.capitalize()
print(group)
# .capitalize() --> სტრინგის პირველი ასო გადაჰყავს upper case-ში,ხოლო ყველა დანარჩენი ასო lower case-ში

# 4. მომხარებელს შემოატანინე სახელი და გვარი ცალ ცალკე, შემდეგ გადააქციე პატარა ასოებად სახელი დაუმატე გვარი ჩვეულებრივად და დაპრინტე.
name = input("enter your name: ").lower()
surname = input("enter your surname: ")
print(name, surname)

# 5. შექმენი ცვლადი name='goalorientedacademy', შემდეგ .find() ფუნქციის მეშვეობით იპოვე ამ სტრინგში:
#   1. 'o'
#   2. 'a'
#   3. 'y'
#   4. 'x'.

name='goalorientedacademy'
print(name.find("o"))
print(name.find("a"))
print(name.find("y"))
print(name.find("x"))