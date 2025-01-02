# შექმენით ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა
list = ["cherry", "kiwi", "dragonfruit", "passionfruit", "pomegranate"]
print(len(list))

# შექმენთ 2 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 3-3 ცვლადი
nums = [1, 2, 3, 4]
nums.append(5)
nums.append(6)
nums.append(7)
numbers = [100,200,300,400]
numbers.append(500)
numbers.append(600)
numbers.append(700)

# შექმენით 2 ლისტი. პირველს მე5ე და მე2ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე3ე და მე4ე ადგილას
list1 = ["cherry", "kiwi", "dragonfruit"]
list2 = ["computer", "headphones", "keyboard", "mouse pad"]

list1.insert(5, "pomegranate")
list1.insert(2,"watermelon")

list2.insert(3,"mouse")
list2.insert(4,"headset")

# შექმენით 2 ლისტი და ორივედან ამოშალეთ 2-2 ცვლადი pop ფუნქციის გამოყენებით
names = ["dato", "irakli", "sandro"]
names.pop(1)
names.pop(2)
print(names)
names2 = ["mari", "lika", "liza"]
names2.pop(0)
names2.pop(2)

# შექმენით 1 ლისტი და გამოიყენეთ ყველა ფუნქცია რაც დღეს გავიარეთ
list3 = ["computer", "headphones", "keyboard", "mouse pad"]
len(list3)
list3.append("headset")
list3.insert(0, "mouse")
list3.pop(1)

# შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში
name = "Lika"
surname = "Chkhikvadze"
status = "English mentor"
print(len(name),len(surname),len(status))