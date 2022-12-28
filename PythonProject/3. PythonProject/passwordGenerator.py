import string
import secrets

l = string.ascii_letters 
d = string.digits 
sc = string.punctuation

alphabet = l+d+sc

password_length = 16
temp=""
for i in range(password_length):
    temp = temp +''.join(secrets.choice(alphabet))
print('Password is: ',temp)
