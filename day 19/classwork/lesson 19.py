# 1. ცვლადში შეინახეთ რიცხვი, თუ ეს რიცხვი ნაკლები იქნება 18-ზე, დაპრინტეთ (underage), თუ იქნება 18-ის ტოლი, დაპრინტეთ (teen), თუ იქნება 18-ზე მეტი (adult).
num = 14
if num < 18:
    print("underage")
elif num == 18:
    print("teen")
elif num > 18:
    print("adult")

# 2. მომხარებელს ცვლადში შემოატანინე რიცხვი, თუ ის რიცხვი უარყოფითია დაუპრინტე (negative), თუ დადებითია (positive), თუ ნულია (zero).
user_num = int(input("enter a number: "))
if user_num < 0:
    print("negative")
elif user_num > 0:
    print("positive")
elif num == 0:
    print("zero")
