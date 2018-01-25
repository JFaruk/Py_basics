    # string_1= 'hello world'
# print(string_1[6])


# slicing  begining end and step slice
# print(string_1[8:])

# print(string_1[:3])

# define starting and ending point
s1='abcdefg'

print(s1[2:5])


s1='abcdefg'

print(s1[:3])



v1='Aminul Islam'

print(v1[:11])
print(v1[-8])
# Grab full string
print(v1[::])
print(v1[:])

# step size 2
print(v1[::2])


#upper case
x=v1.upper()
print(x)

#capitalize
x=v1.capitalize()
print(x)

#split

spli=v1.split()

print(spli)


# print formatting method of string_1

x="Insert another String here:{}".format("Insert me!")

print(x)

# insert multi string
x= 'item one:{y} item two:{x}'.format(x='dog',y='cat')
print(x)


speed=90
if speed >=100:
    printf('License and regestration please')
elif speed<=90:
    print("Please be in limit")






# method most used for string
# split()-> return a list of substring split the string, upper()-> make the all character upper case, lower()-> make the string lower case, split()->returns a string with whitespace removed from front and end. string.replace('old','new')
