# 1. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი indexing-ის მეშვეობით გამოიტანეთ მეორე ელემენტი.
list = ["cherry", "kiwi", "dragonfruit", "passionfruit"]
print(list[1])

# 2. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი შეცვალეთ მეორე ინდექსი სხვა მნიშვნელობით.
list2 = ["apple", "strawberry", "tangerine", "orange"]
list2[2] = "watermelon"
print(list2)

# 3. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (positive indexing).
list3 = ["computer", "headphones", "keyboard", "mouse pad"]
print(list3[0:2])

# 4. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (negative indexing).
list4 = ["computer", "headphones", "keyboard", "mouse pad"]
print(list4[-5:-2])

# 5. შექმენით სია, სადაც გექნებათ 6 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეოთხე ელემენტი (negative indexing & positive indexing).
list5 = ["cherry", "kiwi", "dragonfruit", "passionfruit", "pomegranate", "orange"]
print(list5[-7:4:2])