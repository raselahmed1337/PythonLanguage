# Function Parameter or Argument
# 1.Required Argument
# 2.Keyword Argument
# 3.Default Argument
# 4.Variable-Length Argument

# 1.Required Argument
# def add(a,b,c):
#     return a+b+c
# print(add(1,2,3))

# 2.Keyword Argument
# def add(a,b,c):
#     return a+b+c
# print(add(c=11,a=32,b=43))

# 3.Default Argument
# def add(a,b,c=3):
#     return a+b+c
# print(add(1,4,c=10))

# 4.Variable-Length Argument
# def add(*args):
#     print(list(args))
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# temp = add(1,2,3,4,5,6,7,8,9)
# print(temp)


                        ## map(func,iterators)
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def square(x):
#     return x*x
# newlist = map(square, mylist)
# print(list(newlist))


## Filer()
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x):
    for i in mylist:
        if i%2==0 or i%x==0:
            return True
        return False

temp = filter(is_even,mylist)
print(list(temp))