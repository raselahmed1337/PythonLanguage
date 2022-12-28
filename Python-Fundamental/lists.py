a = ['rasel','ahmed','alex',0,1,2,3,4]
print(a[:-5])

a[1]="ryan" #update the list
a.append("hello") # insert at the end
a.insert(2,"fbi")  # insert in the exact position
a.extend(['miran','ahmed','ahmed','miru']) # to extend the list
a = a+['nayem','miraz','musfique'] # to extend the list
print(a,"\n")

# removing part
del a[0]
a.pop()
print(a)

#counting part
print(a.count('ahmed'))
print(a.count('ahmed')== a.count('ahmed'))

#reverse part
a.reverse()
print(a)


#sort
numlist = [1,2,3,4,523,3,4,6]
numlist.sort()
print(numlist)