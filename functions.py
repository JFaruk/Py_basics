# default layout of fun:

# def my_function(param='default'):
#     pass




# code start from here:
def my_function(param='faruk'):
    '''
    This is the docs  of this function param
    '''
    print('My name is {}'.format(param))


my_function()



# difference between print statement and return statement:

def hello():
    print('hello raja')

hello()
#this will print 'hello raja'


def hello():
    return('hello raja')

hello()
# this one will not give any output because its returning something which need to be store

welcome=hello()
print(welcome)


# finding out type input

def addNumber(m1,m2):
    if type(m1)==type(m2)== type(10):
        return m1+m2
    else:
        print('Please Kindly enter valid integer')
# adding= addNumber(4,5)
adding= addNumber(4,6)
print(adding)
print(type(adding))


#lambda expression

#lampda function used when we need to use that function one time .
lam_list=[1,2,3,4,5,6,7,8,9,10]

# def even_check(number):
#      return number%2 ==0

result_even=filter(lambda number: number%2 == 0,lam_list)
print(list(result_even))



tweet= 'Go sport! #Sports'

a=tweet.upper()
b=tweet.lower()
c=tweet.split()
result= tweet.split('#')[0]
print(result)

print(a)
print(b)
print(c)
