array = [1,2,1,2,4,2,3,5,2,1,6,2,4,8,2,1]

def bruteForce(array,k,tolerance):
    for i in range(len(array)):
        temp = array[i+1:i+k+1]
        if (len(temp)==k):
            for j in range(i+1,len(array)):
                counter = 0
                tempTol = tolerance
                valid = 1
                for z in range(k):
                    if (temp[z]==array[j]):
                        counter+=1
                    elif (temp[z]!=array[j]):
                        tempTol -=1
                    if (tempTol<0):
                        valid =0
                        break
                if (valid==1):
                    print(array[i:i+k])
                    print(temp[:])

bruteForce(array,3,1)
