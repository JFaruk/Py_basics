# python version of hashtable
# create mapping with key-value pairs

dics={'key':1,'key2':'2','dics2':{'num_1':1,'num_2':'abd','num_3':[1,2,'grab the cookie']}}

print(dics['dics2']['num_3'][2].upper())


# example from myself
dic_ex={'sharifa':'200','nafisa':'4000','divine_it':{'IT':'86','CEO':3,'other':[3,5,6,'Faruk']}}

print(dic_ex['nafisa'])
print(dic_ex['divine_it']['other'][3].lower())


my_stuff ={'lunch':'pizza','bfast':'eggs'}
print(my_stuff['lunch'])
my_stuff['lunch']='chicken'

# add new pairs

my_stuff['tea']= 'coffee'
print(my_stuff['lunch'])


print(my_stuff)
