print("(comp): Hello, how are you?")
user_response = input("(user): ")
print("(comp): Great, that you are", user_response + "! What is your name?")
user_name = input("(user): ")
print("(comp): Hello,", user_name + "! How old are you?")
user_age = int(input("(user): "))

    
current_year = 2024
birth_year = current_year - user_age
birth_year2 = birth_year - 1
    
print("(comp): I see, you were born in year", birth_year, "? Let me know if it is True or False?")
birth_year_correct = input("(user): ")

if birth_year_correct.lower() == "true":
    print("(comp): Great, then", birth_year, "is your birth year!")
else:
    print("(comp): Oops, seems I made a mistake. Then ", birth_year2  ,"is your birth year!")


