# def is_prime(n):
#     for i in range(2, n):
#         if (n%i==0):
            
#             return False
#         else:
            
#             return True


# n= int(input("Enter num to check prime"))
# is_prime(n)
# print("Number is prime : ",is_prime(n))



# n= int(input("Enter to print upto n"))
# l1= [1,2]
# for i in range(2,n):
#         if is_prime(i):
#             l1.append(i)
# print(l1)


# k= int(input("enter to print n num"))
# l2=[]
# while (len(l2)==k):
#     i=2
#     if is_prime(i):
#         l2.append(i)
#         i=i+1
# print(l2)



# n6= int(input("enter"))
# for i in range(0,n6+1):
#     print(" "* (n6-i), "*"* ((i*2)-1))
# for i in range(0,n6+1):
#     print(" "* (i), "*" * (((n6-i)*2)-1))

# str1= input("enter")
# ch1= input("enter")
# ch2=input("replace")

# print(str1.count(ch1))
# print(str1.replace(ch1,ch2,2))


# s1= input("ee")
# s2= input("en")
# n=int(input("ent"))
# s3=s1
# s1= s2[:n]+s1[n:]
# s2= s3[:n]+s2[n:]

# print(s1,"\n", s2)


# def character(ch):
    
#     if ch.isalpha():
#         print("it is a letter")
#         if ch.isupper():
#             print("it is a uppercase letter")
#         else:
#             print("it is lowercase letter")   
#     elif ch.isdigit():
#         print("it is a digit")
#         if ch == "0":
#             print("ZERO")   
#         elif ch == "1":
#             print("ONE")
#         elif ch == "2":
#             print("TWO")                  
#         elif ch == "3":
#             print("THREE")  
#         elif ch == "4":
#             print("FOUR")  
#         elif ch == "5":
#             print("FIVE")  
#         elif ch == "6":
#             print("SIX")  
#         elif ch == "7":
#             print("SEVEN")
#         elif ch == "8":
#             print("EIGHT")
#         elif ch == "9":
#             print("NINE")  
#     else:
#         print("it is a special character")   


# k=input("enter")
# print(character(k))






# l3=[]
# s4=input("e")
# s5= input("E")
# l1=s5.split()
# print(l1)
# for l1 in s4:
#     print("Y")



# l3=[]
# s4=input("e")
# s5= input("E")
# if s5 in s4:
#     for i in range(len(s5)):
#         if s4.startswith(s4,i):
#             l3.append(i)
#     print(l3)
# else:
#     print(-1)



# f= open("file.txt","r")
# s= f.read()
# print("All character length", len(s), len(s.split()), len(s.splitlines()))

# d={ }
# for ch in s:
#     d[ch]= d.get(ch,0)+1

# print(d)


import numpy as np



def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeterminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
    return determinant

A=[[45,23,12],[57,21,33],[84,12,34]]
print(getMatrixDeterminant(A))







# Program to find determinant, adjoint, cofactors and inverse of a matrix
import numpy as np
def findinv(a):
    row,column=a.shape
    cof=np.eye(row)
    for i in range(0,row,1):
        for j in range(0,column,1):
            temp=a
            temp=np.delete(temp,i,0)
            temp=np.delete(temp,j,1)
            d=np.linalg.det(temp)
            cof[i,j]=((-1)**(i+j))*d
    adj=cof.transpose()
    determ=np.linalg.det(a)
    inverse=(1/determ)*adj
    print("Determinant is: ",determ)
    print("Cofactor matrix is: \n",cof)
    print("Adjoint of matrix is:\n",adj)
    print("Inverse of matrix is :\n",inverse)

import numpy as np
A=[[4,2,1],[6,4,2]]
M=np.matrix(A)
x=M.shape
print("Matrix is :\n",M)
if x[0]!=x[1]:
    print("Please enter square matrix!")
elif  np.linalg.det(M)==0.0:
    print("Determinant is 0!  \n  Matrix is not invertible!")
else:
    findinv(M)







#Program for printing echelon and row reduced echelon form.


def PerformErow(a,ts,sprint):
    exec(ts)
    if sprint==1:
        if ts=="a[2]=a[2]+3*a[0]":
            print('After performing elementary row operation:',ts)
            print("Echelon form is;\n",a)
        elif ts=="a[1]=a[1]-(a[1,2])*a[2]":
            print('After performing elementary row operation:',ts)
            print("Row Reduced Echelon form is;\n",a)
        else:
            print('After performing elementary row operation:',ts,'\n',a)
        
def rank(matrix):
    x=np.shape(matrix)
    r=0
    for i in range(x[0]):
        for j in range(x[1]):
            if a[i,j]>0:
                r+=1
    return r


import numpy as np
a=np.matrix([[1,2,3],[2,4,4],[-3,5,7]],float)
print("Matrix is:\n",a)
sprint=int(input("Enter 1 for step by step operation. \nEnter 2 for printing only echelon form.\n: "))
PerformErow(a,"a[1]=a[1]-2*a[0]",sprint)
PerformErow(a,"a[2]=a[2]+3*a[0]",sprint)
if sprint==2:
    print("Echelon form is: \n",a)
PerformErow(a,"a[[1,2]]=a[[2,1]]",sprint)
PerformErow(a,"a[1]=a[1]/11",sprint)
PerformErow(a,"a[0]=a[0]-2*a[1]",sprint)
PerformErow(a,"a[2]=a[2]/(-2)",sprint)
PerformErow(a,"a[0]=a[0]-(a[0,2])*a[2]",sprint)
PerformErow(a,"a[1]=a[1]-(a[1,2])*a[2]",sprint)
if sprint==2:
    print("Row reduced echlon form is:\n",a)
R=rank(a)
print("Rank of matrix is : ",R)




#Solve a system of equations using gauss elimination

import numpy as np
n=int(input("Enter number of variables: "))
a=np.zeros((n,(n+1)))
x=np.zeros(n)
print('Enter coefficients of augmented matrix: ')
for i in range(n):
    for j in range(n+1):
        a[i,j]=float(input('a['+str(i)+','+str(j)+']='))

for i in range(n):
    if a[i,i]==0.0:
        sys.exit('Division by zero! ')
    for j in range(i+1,n):
        ratio=a[j,i]/a[i,i]
        for k in range(n+1):
            a[j,k]=a[j,k]- ratio*a[i,k]
print('\nMatrix after forward phase:\n',a)

x[n-1]=a[n-1,n]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    x[i]=a[i,n]
    for j in range(i+1,n):
        x[i]=x[i]-a[i,j]*x[j]
    x[i]=x[i]/a[i,i]

print('\nSolution: ')
for i in range(n):
    print('X%d = %0.2f'%(i,x[i]))







# Program to find solutions of homogeneous equations using gauss jordan method.
import numpy as np
import sys
n=int(input("Enter no. of variables: "))
a=np.zeros((n,(n+1)))
x=np.zeros(n)
ratio=0
print("Enter matrix coefficients: ")
for i in range(n):
    for j in range(n+1):
            a[i,j]=float(input(('a['+str(i)+']['+str(j)+']=')))
for i in range(n):
    if a[i,i]==0.0:
                sys.exit('Division by zero!')
    for j in range(n):
            if i!=j:
                ratio+=a[j,k]/a[i,i]
            for k in range(n+1):
                        a[j,k]=a[j,k]-ratio*a[i,k]

for i in range(n):
    x[i]=a[i,n]/a[i,i]

print("\nRequired solution is: ")
for i in range(n):
        print("X%d=%0.2f"%(i,x[i]),end='\t')






#Program to find simplified span of a given set of vectors. 
M=[[1,0,1,3],[2,3,4,7],[-1,-3,-3,-4]]
A=np.matrix(M) 
print("Row space (or simplified span) of given set of vectors :")
print(A.rowspace())


#Program to find nullspace or solution space of given vector set
M=[[1,0,1,3],[2,3,4,7],[-1,-3,-3,-4]]
A=np.matrix(M)
print("Null space of given set of vectors :")
print(A.nullspace())















        