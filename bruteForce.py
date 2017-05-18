array = [1,2,1,2,4,2,3,5,2,1,6,2,4,8,2,1]
def areMotif(arr1,arr2,k,tolerance):
    i=0
    j=0
    counter = 0
    while (i,j < k-1):
        if(arr1[i]==arr2[j]):
            counter +=1
        elif(arr1[i]!=arr2[j]):
            tolerance-=1
            counter+=1
        if(tolerance<0):
            return False
        elif (counter==k) :
            return True
        i+=1
        j+=1

def bruteForce(array,k,tolerance):
    for i in range(len(array)):
        temp = array[i:i+k]
        if (len(temp)==k):
            for j in range(i+1,len(array)):
                if(j+k<=len(array)-1 and areMotif(temp,array[j:j+k],k,tolerance)==True):
                    print(temp[:])
                    print(array[j:j+k])


bruteForce(array,3,1)
