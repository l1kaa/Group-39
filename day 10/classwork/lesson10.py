# for loops
# task 1 - გამოიტანეთ მხოლოდ კენტი რიცხვები 50-დან 150-მდე :
for i in range(49,150,2):
    print(i)

# task 2 - მომხმარებელს შემოატანინეთ რაიმე წინადადება და გამოიტანეთ ამ წინადადების თითოეული ასო ცალცალკე:
sentence = input("please enter a sentence:")
for i in sentence:
    print(i)


# while loops
# task 1 - გამოიტანეთ მხოლოდ ლუწი რიცხვები 500-დან 700-მდე:
i = 500
while i < 700:
    print(i)
    i += 2


# task 2 - გამოიტანეთ რიცხვები 50-დან 0-მდე:
i = 50
while i > 0:
    print(i)
    i -= 1



# BOSS LEVEL - ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ რიცხვი იქმადე სანამ არ დაემთხვევა თქვენს რიცხვს:
fav_num = 14
user_num = " "
while user_num != fav_num:
    user_num = int(input("please enter any number:"))
print("you've succesfully guessed my favorite number")