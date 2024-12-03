numbers = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
print(numbers[:5]) #პირველი ხუთი რიცხვი
print(numbers[::3]) #ყოველი მესამე რიცხვი
new_numbers = numbers[:5] + numbers[::3]
print(len(new_numbers))