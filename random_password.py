import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
special_char="@#$%^&*_?"
comb=upper+lower+special_char
password_length=8
password="".join(random.sample(comb,password_length))
print(password)