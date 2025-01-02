# 1. შეინახეთ სამი ქალაქის სახელი ცალკე ცვლადში და დაპრინტეთ ისინი.
city1 = "Paris"
city2 = "Milan"
city3 = "Lyon"
print(city1, city2, city3)

# 2. შეართეთ ორი სიტყვა (მაგ., სახელი და გვარი) და დაპრინტეთ სრული სახელი.
name = "Lika"
surname = "Chxikvadze"
print(name + " " + surname)

# 3. აიღეთ ორი რიცხვი და დაპრინტეთ მათი ჯამი, სხვაობა, ნამრავლი და განაყოფი.
num1 = 14
num2 = 4
print(num1 + num2) #ჯამი
print(num1 - num2) #სხვაობა
print(num1 * num2) #ნამრავლი
print(num1 / num2) #განაყოფი

# 4. მიანიჭეთ ერთი ცვლადის მნიშვნელობა მეორეს და დაპრინტეთ ორივე ცვლადი, რომ ნახოთ შედეგი.
fruit = "kiwi"
fruit = "passion fruit"
print(fruit)

# 5. შემოატანინეთ მომხმარებელს მისი საყვარელი ფერი და დაპრინტეთ წინადადება, რომელშიც ეწერება ეს ფერი.
color = input("what's your fav color?: ")
print("user's fav color is", color)

# 6. შეინახეთ სტრინგი, მთელი რიცხვი და float სამ განსხვავებულ ცვლადში და დაპრინტეთ მათი ტიპები.
var1 = "Lika"
var2 = 39
var3 = 34.5
print(type(var1))
print(type(var2))
print(type(var3))

# 7. აიღეთ float რიცხვი, გადააკეთეთ იგი მთელ რიცხვად და შემდეგ დაპრინტეთ როგორც ორიგინალური float, ასევე გადაყვანილი მთელი რიცხვად.
float = 3.5
print(float)
print(int(float))

# 8. შეინახეთ რიცხვი ცვლადში და შეამოწმეთ მისი მონაცემთა ტიპი `type()` ფუნქციით. დაპრინტეთ შედეგი.
item = "headphones"
print(type(item))

# 9. ორ რიცხვზე შეასრულეთ  არითმეტიკული მოქმედებები (შეკრება, გამოკლება, გამრავლება, გაყოფა) და შედეგები შეინახეთ ცვლადებში. შედეგების დაპრინტეთ.
num3 = 25
num4 = 5
addition = print(num1 + num2) #ჯამი
Subtraction = print(num1 - num2) #სხვაობა
Multiplication = print(num1 * num2) #ნამრავლი
division = print(num1 / num2) #განაყოფი

# 10. აიღეთ სამი სტრინგი და გააერთიანეთ ისინი ერთ წინადადებად. დაბეჭდეთ საბოლოო წინადადება.
str1 = "This"
str2 = "is"
str3 = "a computer"
print(str1,str2,str3)

# 11. შეინახეთ ორი რიცხვი ცალკეულ ცვლადებში და გამოიყენეთ შედარების ოპერატორები (`<`, `>`, `<=`, `>=`, `==`, `!=`) შედარებისთვის. დაპრინტეთ თითოეული შედარების შედეგი.
numm1 = 44
numm2 = 39
print(numm1 < numm2)
print(numm1 > numm2)
print(numm1 <= numm2)
print(numm1 >= numm2)
print(numm1 == numm2)
print(numm1 != numm2)

# 12. შექმენით ცვლადები ორი სხვადასხვა ასაკისათვის. გამოიყენეთ შედარების ოპერატორები იმის შესამოწმებლად, არის თუ არა ერთი ასაკი მეორეზე დიდი ან მისი ტოლი. დაპრინტეთ შედეგი.
age1 = 14
age2 = 40
print(age1 > age2)
print(age1 == age2)

# 13. სამ ცვლადს მიანიჭეთ რიცხვითი მნიშვნელობები. გამოიყენეთ შედარების ოპერატორები, რათა შეამოწმოთ არის თუ არა პირველი ცვლადი მეორეზე ნაკლები და თუ მეორე მესამეზე ნაკლები. დაპრინტეთ შედეგები.
Num1 = 55
Num2 = 67
Num3 = 88
print(Num1 < Num2 < Num3) 

# 14. ცვლადში შეინახეთ ორი სხვადასხვა სტრინგი და შეადარეთ ისინი ტოლობის (`==`) და უტოლობა (`!=`) ოპერატორების გამოყენებით. დაპრინტეთ ამ შედარების შედეგები.
username1 = "Lika"
username2 = "lika"
print(username1 == username2)
print(username1 != username2)


# 1. Write an if-else statement that prints "Good morning!" if the current hour is before 12, and "Good afternoon!" if it is 12 or later.
current_hour = 13
if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

# 2. Create an if-else statement to check if the temperature exceeds 30 degrees. If it does, print "It's hot outside!"; otherwise, print "It's not too hot."
temperature = 30
if temperature > 30:
    print("It's hot outside!")
else:
    print("it's not too hot")

# 3. Create an if-else statement to determine if a person is a teenager. If the age is less than 19 print "You are a teenager!"; otherwise, print "You are not a teenager."
user_age = 18
if user_age < 19:
    print("You are a teenager!")
else:
    print("You are not a teenager")