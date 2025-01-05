# 1. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ 5 რიცხვი და დაპრინტეთ ამ list-იდან მაქსიმალური რიცხვი.
list1 = [100, 200, 300, 400, 500]
print(max(list1))

list2 = [750, 890, 34, 28999, 568]
print(max(list2))

list3 = [7.7, 4.5, 0.9, 9.999, 10.5]
print(max(list3))

# 2. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ 5 რიცხვი და დაპრინტეთ ამ list-იდან მინიმალური რიცხვი.
list4 = [100, 200, 300, 400, 500]
print(min(list4))

list5 = [750, 890, 34, 28999, 56]
print(min(list5))

list6 = [7.7, 4.5, 0.9, 9.999, 10.5]
print(min(list6))


# 3. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ მინიმუმ 5 ელემენტი და დაპრინტეთ ამ list-ის სიგრძე.
fruit = ["apple", "pear", "kiwi", "tangerine", "melon", "watermelon"]
print(len(fruit))

items = ["headphones", "microphone", "mousepad", "PC", "disk"]
print(len(items))

nums = [1,2,3947,4,566,6,7,834,9,388,5009]
print(len(nums))

# 4. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ 5 რიცხვი და დაპრინტეთ ამ list-იდან რიცხვების ჯამი.
numbers = [3947,566,6,7,834]
print(sum(numbers))

numbers2 = [750, 890, 34, 28999, 56]
print(sum(numbers2))

numbers3 = [566, 899, 37, 68, 908]
print(sum(numbers3))

# 5. შექმენით 4 სხვადასხვა list-ი, თითოში დაამატეთ მინიმუმ 10 ელემენტი
# და დაპრინტეთ:
#  1) პირველ list-ის პირველიდან მეოთხე ელემენტამდე ცვლადები.
names = ["dato", "irakli", "lika","liza", "sandro", "andria", "data", "toko", "ana", "nini"]
print(names[:4])

#  2) მეორე list-ის მეოთხედან მერვე ელემენტამდე ცვლადები ფორ ციკლის გამოყენებით.
numberss = [1,2,3,4,5,6,7,8,9,10]
for i in numberss:
    print(numbers[3:9])

#  3) მესამე list-ის მეცხრედან მეექვსე ელემენტამდე ცვლადები გაითვალისწინეთ არა 6დან 9მდე არამედ 9დან 6მდე გამოიყენეთ უარყოფითი რიცხვები.
Numbers = [250,350,600,780,473,90,700,356,879,1000]
print(Numbers[-2:-4])
#  4) მეოთხე list-ში დაპრინტეთ მისი ყველა ცვლადი while ცოკლის გამოყენებით.
fruits = ["apple", "pear", "kiwi", "tangerine", "melon", "watermelon", "grapes", "banana","peach", "lemon"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# (boss level);
# 6. შექმენით def ფუნქცია რომელიც არგუმენტად აიღებს list-ს რომელშიც მომხმარებელი შეიყვანს მინიმუმ 5 რიცხვს და დაპრინტავს ამ list-ის მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და list-ის სიგრძეს.
def inputs(numbers):
    numbers = [int(input("Enter a number: ")) for _ in range(5)]
    return max(numbers), min(numbers), sum(numbers), len(numbers)
print(inputs)