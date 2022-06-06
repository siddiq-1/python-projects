import email
import re
'''
a-z gmail starts with alphabet
0-9 digits 
".""_" should be one time
@sign should be one time 
. position should be on 2, 3 negative indices 
'''
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter the email: ")

if re.search(email_condition,user_email):
    print("Right email")
else:
    print("Wrong email")