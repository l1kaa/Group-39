# 1. სიაში შეინახეთ 5 რიცხვი, შემდეგ კი დარპინტეთ პირველი და მეოთხე ელემენტების ნამრავლი.
numbers = [100, 200, 300, 400, 500]
print(numbers[0] * numbers[3])

# 2. სიაში შეინახეთ 7 სტრინგი, შემდეგ დაპრინტეთ შუა სტრინგი.
list = ["strawberry", "apple", "cherry", "kiwi", "dragonfruit", "passionfruit", "pomegranate"]
print(list[3])

# 3. ცვლადში შეინახეთ სტრინგი, შემდეგ კი დაპრინტეთ ამ სტრინგის მხოლოდ მეორე ასო.
string = "Lika"
print(string[1])

# 4. შექმენით ვენდინგ მანქანის თამაში პითონის მეშვეობით, როგორც გაკვეთილზე გავაკეთე, უნდა გქონდეთ 
# პროდუქტები, მომხმარებელს უნდა შეეძლოს არჩევა რიცხვის მიხედვით, შემდეგ კი უნდა დაუპრინტოს ის პროდუქტი, რომელიც ამოირჩია, პროდუქტები შეინახეთ სიაში.
products = ["protein bar", "water", "Energy drink"]
users_choice = int(input("choose a product you'd like to buy: 1)protein bar; 2)water; 3)Energy drink: "))
print(products[users_choice])