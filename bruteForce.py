import time
import random
import math
def randomDataSetGen(lines,length,mode):
    array = []
    if mode=="num":
        for i in range(lines):
                inside = [random.sample(range(10),1) for item in range(length)]
                array.append(inside)
    elif mode=="string":
        for i in range (lines):
            inside = [chr(random.randint(65,90)) for item in range(length)]
            array.append(inside)
    return array

def writeToFile(array):
    f = open("./data.txt","w")
    for i in range(len(array)):
        for j in range(len(array[i])):
            f.write(array[i][j])
        f.write("\n")

def readFromFile(array):
    f = open("./data.txt","r")
    i=0
    for line in f:
        array[i]=list(line[:-2:])
        i+=1

    return array

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
#<----------------------------------------------------------------------------------------------->

arr =randomDataSetGen(10,100,"string")
writeToFile(arr)
readFromFile(arr)
timeArr=[]
for element in arr:
    start_time = time.time()
    bruteForce(element,3,1)
    print ("<------------NEXT-LINE------------>")
    elapsed_time = time.time() - start_time
    timeArr.append(elapsed_time)
print timeArr
