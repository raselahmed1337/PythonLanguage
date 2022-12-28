##if,elif,else
a = int(input("enter a number:"))
if a>10:
    print("input value is greater than 10")
elif a<10:
    print("input value is less than 10")    
else:
    print("input value is equal 10") 

##check value is 0 or not?
a=0
if a:
    print(True)
else:
    print(False) 


## nested loop
a= int(input("enter a number: "))

if a<10:
    if a%2==0:
        print('less , yes')
    else:
        print('less, no')    
else:
    if a%3==0:
        print('greater , yes')
    else:
        print('greater, no')  


# # #problem 1::
## the user will input an integer, if the number is divisible by 3 and 5.
## the output will be yes, and otherwise the output will be no

userNumber = int(input('enter an input here: '))
if userNumber%3==0 and userNumber%5==0:
    print('YES')
else:
    print('NO')



# # # problem 2::
## user will input a number. if the number is positive, the output will be positive
## if it is negative, the output will be negative and if it is zero
## the output will be ZERO

userNumber = int(input('Enter a number: '))
if userNumber>=0:
    print('Positive')
else:
    print('Negative')


# # # problem 3::
## user will inpout an integer. if the number is even then the output will  be
## even and if it is odd the output will be odd.
userNumber = int(input('Enter a number: '))
if userNumber%2==0:
    print('Even')
else:
    print('odd')


# # # problem 4::
## user will input a character . if the char. is vowel. the output iwll be the VOWEL
## if it is consonent, it will be consonent. if the character,  doesnt fall within the alphabet the will be nothing

userChar = input('user input char: ')

if userChar>='a' and userChar<='z' or userChar>='A' and userChar<='Z':
    if userChar in 'aeiouAEIOU':
        print('vowel')
    else:
        print('consonent')
