# 1)შექმენით ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა
list = ["cherry", "kiwi", "dragonfruit", "passionfruit", "pomegranate"]
print(len(list))

# 2)შექმენთ 3 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 2-2 ცვლადი
nums = [1, 2, 3, 4]
nums.append(5).append(6)

numbers = [100,200,300,400]
numbers.append(500).append(600)

floats = [6.7, 9.99, 45.5]
floats.append(66.7).append(8.99)

# 3)შექმენით 2 ლისტი. პირველს მე3ე და მე0ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე4ე და მე2ე ადგილას
list1 = ["cherry", "kiwi", "dragonfruit"]
list2 = ["computer", "headphones", "keyboard", "mouse pad"]

list1.insert(3, "pomegranate")
list1.insert(0,"watermelon")

list2.insert(3,"mouse")
list2.insert(2,"headset")

# 4)შექმენით 1 ლისტი და ორივედან ამოშალეთ 2 ცვლადი pop ფუნქციის გამოყენებით
items = ["book", "pen", "pencil", "sharpener"]
items.pop(0).pop(3)

# 5)შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში
name = "Lika"
surname = "Chkhikvadze"
status = "English mentor"
print(len(name),len(surname),len(status))

# 6)კომენტარების გამოყენებით ახსენით რას აკეთებს თითოეული ფუნქცია

# < built-in functions - ჩაშენებული ფუნქციები >

# len() --> აბრუნებს სიის ან სტრინგის ზომას. ამ ფუნქციას არ სჭირდება წერტილი.
# .append() --> სიის ბოლოს ამატებს ელემენტს ↓
#   • ეს ფუნქცია მხოლოდ მუშაობს სიებზე და არა სტრინგებზე, რადგან სიები შეცვლადია(mutable), ხოლო სტრინგები უცვლადი(immutable). სტრინგებზე გამოყენების შემთხვევაში მიიღებს error-ს.
# .insert() --> სიაში ამატებს ელემენტს მოცემულ ინდექსზე. მაგ items.append(1,"product") ↓
#   • ამ ფუნქციას 2 არგუმენტი გადაეცემა. პირველ არგუმენტად გადაეცემა ინდექსი, ხოლო მეორე არგუმენტად სტრინგი.
# pop() --> სიიდან შლის ელემენტს. მას არგუმენტად მხოლოდ ინდექსი გადაეცემა, მაგ. items.pop(1)