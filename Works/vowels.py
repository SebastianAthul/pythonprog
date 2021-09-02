vowels="aeiou"
user=input("Enter the string: ")
count=0
for i in user:
    if i in vowels:
        count=count+1
print("NO:OF VOWELS =",count)
