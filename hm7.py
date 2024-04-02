word = ""
seen_chars = set()

while True:
    char = input("Введіть символ: ")
    
    if char == ".":
        break
    
    if char in seen_chars:
        print("Послідовні дублікати не дозволені, ви ввели:", word)
        break
    
    word += char
    seen_chars.add(char)
    
    if word == word[::-1]:
        print("Це паліндром:", word)
        break
