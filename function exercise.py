
def arrayCheck(num):
    '''
    Prob:1

    '''
    for i in range(len(num)-2):
        if num[i]==1 and num[i+1]==2 and num[i+2]==3:
            return True
    return False


result1= arrayCheck([1,2,3,1,2,4,5,6])
result2=arrayCheck([2,3,5,2,1,2,5,4])
print(result1)
print(result2)
