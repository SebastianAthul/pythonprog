punc= "!@#$%^&*()_+{}|:<>?[]',./"
string=input("ENTER A STRING: ")
nopunc=""
for char in string:
    if char not in punc:
        nopunc=nopunc+char
print(nopunc)







