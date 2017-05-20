array ="ABCABDABCAFkkkkkkkkC" 
def areMotif(arr1,arr2,k,tolerance):
    i=0
    j=0
    counter = 0
    while (i,j < k):
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
    flag = 0
    for i in range(len(array)):
        temp = array[i:i+k]
        if (len(temp)==k):
            for j in range(i+k,len(array)):
                if(j+k<=len(array) and areMotif(temp,array[j:j+k],k,tolerance)==True):
                    if (flag != 1):
                        print(temp[:])
                    flag = 1
                    print(array[j:j+k])
            print
            flag = 0


bruteForce(array,3,1)
