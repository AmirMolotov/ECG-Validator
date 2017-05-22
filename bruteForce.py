import time
import random
import math
def randomDataSetGen(lines,length,mode):
   array = []
   if mode=="num":
       for i in range(lines):
               inside = [chr(random.randint(48,57)) for item in range(length)]###
               array.append(inside)
   elif mode=="string":
       for i in range (lines):
           inside = [chr(random.randint(65,90)) for item in range(length)]###
           array.append(inside)
   return array
def writeToFile(array):
   f = open("./input.txt","w")
   for i in range(len(array)):
       for j in range(len(array[i])):
           f.write(array[i][j][0])
       f.write("\n")
def readFromFile(array):
   f = open("./input.txt","r")
   i=0
   for line in f:
       array.append(list(line[:-2:]))
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
       flag2 = 0
       temp = array[i:i+k]
       if (len(temp)==k):
           for j in range(i+k,len(array)):
               if(j+k<=len(array) and areMotif(temp,array[j:j+k],k,tolerance)==True):
                   if (flag != 1):
                       print(temp[:])
                       for t in range(len(temp)):
                           f.write(temp[t])
                       f.write(" ")
                   flag = 1
                   flag2 = 1
                   for q in range (j+k-j):
                        f.write(array[j+q])
                   f.write(" ")
                   print(array[j:j+k])
           if (flag2 == 1):
               print
               f.write("\n")
           flag = 0
#<----------------------------------------------------------------------------------------------->
arr =randomDataSetGen(10,300,"num")
writeToFile(arr)
arr = []
arr = readFromFile(arr)

f = open("./output.txt","a")
for tt in range(20):
    start_time = time.time()
    for element in arr:
       bruteForce(element,tt+1,1)
       f.write("<------------Next-300-Signals------------>\n")
       print ("<------------NEXT-LINE------------>")
    elapsed_time = time.time() - start_time
    print (elapsed_time)
