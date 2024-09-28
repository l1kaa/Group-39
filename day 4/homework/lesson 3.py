#task 1:

name = input("please enter your name: " )
surname = input("please enter your friend's surname: " )

print(name + " " + surname)

#task 2:

age = input("please enter your age: ")
users_age_in_10_years = int(age) + 10
print("your age in 10 years will be:" ), print(users_age_in_10_years)


#task 3:

num1 = input("please choose any number: ")
num2 = input("please choose any number for the second time: ")
num3 = input("please choose any number for the third time:  ")
num4 = input("please choose any number for the fourth time: ")
num5 = input("please choose any number for the last time: ")


arithmetic_mean = (int(num1) + int(num2) + int(num3) + int(num4) + int(num5))/5
print("the arithmetic mean of your chosen numbers is: "), print (arithmetic_mean)

#task 4:

# პითონი არის Case sensitive პროგრამირების ენა, რაც იმას ნიშნავს,რომ პითონი აცევს ყურადღებას ესა თუ ის სიტყვა ან კოდი lowercase-ით იწერება თუ uppercase-ით. აქედან გამომდინარე აუცილებელია,რომ კოდის წერისას და ცვლადის შექმნისას ყურადღება მივაქციოთ იმას, თუ სად გამოვიყენებთ lowercase-ს და uppercase-ს. 
# snake case (_) ვიყენებთ იმისათვის,რომ რაიმე ცვლადის შექმნისას, რამდენიმე სიტყვა ერთმანეთისგან გამოვყოთ. snake case-ის გამოყენების გარეშე, ცვლადის შექმნისას რამდენიმე სიტყვის space-ით გამოყოფა ტერმინალში გამოიტანს error-ს.

#task 5:

#"lika" + 15          #debug: "lika" + "15" სტრინგისა და ინტეჯერის კონკატინაცია არ შეიძლება.
#float("lika")        #debug: ასოების შემცველი სტრინგის float-ად გადაქცევა არ შეიძლება.
#"GOA is the best programming academy'         #debug: "GOA is the best programming academy" or 'GOA is the best programming academy'
#Position = "finance manager"
#print(position)      #debug: print(Position)
#grade in english = "A+"      #debug: grade_in_english = "A+"


#debugging ნიშნავს error-ების შესწორებას.