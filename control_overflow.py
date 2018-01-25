a_v= 'devine'
a_c='devine'

if len(a_v)== len(a_c):
    print('they are same string')

else:
    print('Haha they are different string bitches')

# python does not use triple '=' sign to check for type and value only use normal way.


if 1== '1':
    print('true')
elif 2 != 1:
    print('False')
else:
    print('None are true')


# tuple unpacking
tup_unpack= [(1,2),(4,5),(5,0),(9,0)]
# normal way to iterate:
for pairs in tup_unpack:
    print(pairs)

# unpacking:

for t1,t2 in tup_unpack:
    print(t2)
    print(t1)


# experment on tupple unpacking from google.

def add(a,b):
    return a+b

print(add(4,5))
z=(4,5)
print(add(*z))
# print(add(z))


# x=5
# y=6
#
# y=x
# x=y
#
# print(y)



# while loops
'''
while loops examples
'''
i=1

while i<5:
    print('i is : {}'.format(i))
    i=i+1



i=1

while i<=15:
    print('i is : {}'.format(i))
    i=i+2



# range


range(0,5)

print(list(range(0,5)))



for item_list in range(0,11,3):
    print(item_list)






list=[1,2,3,4,5,6,7,8]

for num in list:
    if num%2==0:
        print('Even : ',num)
    else:
        print('Odd : ',num)    
