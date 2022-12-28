# myfile = open('test.txt','a')
# content = myfile.write('i am student of Computer science')
# print(content)
# myfile.close()


try:
    with open('test.txt', 'r') as myfile:
        print(myfile.read())
except FileNotFoundError:
    print('file not found')
finally:
    print('Code is running well')