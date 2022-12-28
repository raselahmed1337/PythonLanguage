## while loop::
a=1
while a<=10:
    print(a)
    a+=1

##sequence : n*(n+1)/2 
a=1
sum=0
while a<=10:
    sum=sum+a
    print(sum)
    a+=1



## print list
a = ['rasel','ahmed','alex','miraz','shakib',1,2,3,4,5]
for i in a:
    print(i)
print("\n")


###
name = 'RASEL'
lst = []
for letter in name:
    print(letter)
    lst.append(letter)
print(lst)    

### problem solving part::
##Question: a lsit of numbers from 1 to 100. that are divisible by 3 not 5;
lst=[]
for i in range(1,101):
    if i%3==0 and i%5!=0:
        lst.append(i)
print(lst)


##Question: 
#from this list, a list of numbers less than 50 should be created and displayed as output.
my_list = [13,34,56,70,50,30,45,6,7,5,4,43,15,52,65,65,6,6,65,45,3,45,3,5,10]
for items in my_list:
    if items<50:
        print(items)


    
##Question: removes the duplicates in print them
my_list = [13,34,56,70,50,30,45,6,7,5,4,43,15,52,65,65,6,6,65,45,3,45,3,5,10]

a=[]
for items in my_list:
    if items not in a:
        a.append(items)
print(a)