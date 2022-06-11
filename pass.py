
import random
import string


print(" \n 🤖 Welcome To 🔑 Password🔑 Generator : ~ ")


name = input(" \n 🔴 What is your Name? : Real Name 😈 : ~ ")
fword = input(" \n 🔴 What is your favourite name/word ? : ~ ")
whichcom = input(" \n 🔴 For which thing you made password : OPTIONAL : ~ ")

while True:
    try:
        length = int(input(" \n 🔴 How many password length you want ? : ~ "))
        break
    except Exception as e :
        print(f"Please Enter A Big Number : ~ {e}")
        

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))

s.extend(list(s4))

random.shuffle(s)
password = "".join(s[0:length])
print(f" \n This Is Your Strongest Password 🤖  : ~ {name+'-'+fword+'-'+whichcom+'-'+password}")

print("\nThanks For Using Our Tool : ~ Code with Shubhu ❤️\\\n")
