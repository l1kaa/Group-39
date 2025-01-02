# 1. შექმენით ფუნქცია, სადაც გექნებათ 5 სიტყვიანი სია, შემდეგ მომხმარებელს შემოატანინეთ 0-იდან 5-მდე რიცხვი, და დაუპრინტეთ ეგ index თქვენი შექმნილი სიიდან.
def checking_index(words):
    index = int(input("enter a number from 0 to 5: "))
    if index > 5 and index >= len(words):
        return "please enter a valid number"
    else:
        return words[index]
words = ["apple","strawberry",'pear',"kiwi", "melon"]
print(checking_index(words))