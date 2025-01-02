# 1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.
def addition(num):
    return num + 5

# 2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს
def multiplication(int1, int2):
    return int1 * int2

# 3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).
def length(string):
    return len(string)

# 4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).
def length_of_list(list = ["str1", "str2","str3", "str4"]):
    list2 = [len("str1"),len("str2"),len("str3"),len("str4")]
    return list2


# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# 6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
# (მაგალითად: input: "Hello World". output: "HELLO WORLD".)
def uppercase(string):
    return string.upper()