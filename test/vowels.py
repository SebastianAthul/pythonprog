vowels="aeiou"
user=input("enter the string: ")
no_vowels=""
for i in user:
    if i not in vowels:
        no_vowels+=i
print(no_vowels)
