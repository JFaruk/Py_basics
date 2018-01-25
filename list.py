# this file contain all example tried for python "list" or array

mylist=[1,2,4]
mylist[0] = 'abc'
print(mylist)

# length function on list

print(len(mylist))


mylist= ['a','b','c','d', 'abcd',123]

# print(mylist[:-4]) print everything from -4 to first upto -4 but not included
# print(mylist[:-2])
# print(mylist[::])
mylist[4]= 4
print(mylist)
# append() add item to the end of the list
mylist.append('new item')
print(mylist)



#.extend() function use for the extend the new list to current list
list2=['x','y','z']
print(mylist)

print('After use of extend function')
mylist.extend(list2)

print(mylist)


# removing last item from list by .pop() function

poplist=mylist.pop()

print('After poping element from the current list will be like this : ', mylist)


# where did the pop item go? its stored on the variable we saved

print(poplist)

# removing item from list with a index.


poplist_2=mylist.pop(5)

print('after poping the element, list will be like this : ' ,mylist)


# some useful function. reverse and return,sort


colors=['red','black','white','blue','navy']

reversedlist= colors.reverse()

print(colors)
print(colors[:-2])


listnum=[11,23,13,0,2,3,5]
listnum.sort()
print(listnum)


# nested list index and list comprehension

# a normal nested list
nestedlist=[1,2,['a','b','c']]
print(nestedlist[2])

#getting element from nested list
print(nestedlist[2][1])


nestedlist=[1,2,['a','b','c',['x','y',[1,2]]]]
print('way of getting element from multi nested list: ', nestedlist[2][3][2][1])


# another example

matrix=[[1,2,3],[4,5,6,],[7,8,9]]

first_col=[row[0] for row in matrix]
second_col=[row[1] for row in matrix]
third_col=[row[2] for row in matrix]
print(first_col)
print(second_col)
print(third_col)
