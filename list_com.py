# One of the most important topics on py is list comprehension. running a for loop like this and appending something in the list from another list or sequence

x=[2,3,4,5,6]

keep=[]

for item in x:
    keep.append(item**2)

print(keep)

k=[num**2 for num in x]

print(k)


root_num=[100,200,300,400,500,600,700]

root_result=[item**0.5 for item in root_num]
print(root_result)
