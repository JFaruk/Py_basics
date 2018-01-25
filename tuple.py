#Tuples
t1=(1,23,4)

print(t1[2])


# can hold mix data type
t2=(1,'faruk','ccc',4)
print(t2[3])

# slicing
print(t2[-3])


#tuples are immutable means cant assign or change index after assigning them to something

# t2[0]='faruk'
# print(t2)

#this will through a error call  'tuple' object does not support item assignment



# Sets
x=set()
x.add(2)
x.add(3)
x.add(9)
x.add(8)
x.add(0.1)
x.add(6)
x.add(8)
x.add(10)


print(x)


converted=set([1,2,2,2,2,2,1,1,1,3,3,3,5,5,5,4,4])

print(converted)
