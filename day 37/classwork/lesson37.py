# * შექმენი ფუნქცია სახელად max_of_two, რომელიც 
# არგუმენტად იღებს ორ რიცხვს. 
# * ფუნქციამ უნდა დააბრუნოს და დაპრინტოს ამ
# ორი რიცხვიდან უფრო დიდი. 
def max_of_two(int1, int2):
    if int1 > int2:
        return int1
    elif int2 > int1:
        return int2
    else:
        return "the numbers are equal"
print(max_of_two)