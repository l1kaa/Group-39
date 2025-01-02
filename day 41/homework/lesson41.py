# შექმენით ფუნქცია, vending-machine, გექნებათ პროდუქტების სია, მომხმარებელმა, კი უნდა აირჩიოს სასურველი პროდუქტი, თქვენ კი ის უნდა დაუპრინტოთ,

# Bonus:
# თუმცა მომხმარებელს საწყისად უნდა გააჩნდეს რაღაც კონკრეტული თანხა, ხოლო პროდუქტიც რაღაც გაარკეული თანხა უნდა ღირდეს, თუ მომხმარებელს არ ექნება საკმარისი ფული, არ უნდა დაუპრინტოთ შესაბამისი ინდექსის პროდუქტი.

def vending_machine(products,money,choice):
    products = ["protein bar", "water", "snack"]
    money = int(input("enter an amount of money that you have: "))
    choice = input("choose a product: ").lower()
    if choice == "protein bar" and money >= 3.99:
        return(products[0])
    elif choice == "protein bar" and money < 3.99:
        return("you don't have enough amount of money")
    elif choice == "water" and money >= 0.99:
        return (products[1])
    elif choice == "water" and money < 0.99:
        print("you don't have enough amount of money")
    elif choice == "snack" and money >= 2.50:
        return (products[2])
    elif choice == "snack" and money < 2.50:
        return("you don't have enough amount of money")



