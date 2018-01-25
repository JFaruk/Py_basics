#given String
s= 'django'
# output needed 'd','o','djan','jan' ,'go'

print(s[0])
print(s[5])
print(s[:4])
print(s[1:-2])
print(s[4:])

# reassign hello to goodbye

l=[3,7,[1,4,'hello']]
l[2][2]='Goodbye'
print(l[2][2])
print(l)


#using  key and indexing  grabe hello
d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k2':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])   
print(d3['k2'][0]['nest_key'][1][0])

mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
x=set(mylist)

print(x)
age=4
name='samy'

prfo="hello my dog's name is {name} and he is {age} years old".format(name='sammy',age='4')

print(prfo)
