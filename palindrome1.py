def is_palindrome(word):
    new_word =""
    for x in word:
        new_word = x +new_word 
    if new_word == word:
        result = "palindrome"
    else:
        result ="not palindrome"
    return result 
w="abba"
assert is_palindrome(w) == "palindrome"

print(is_palindrome(w))