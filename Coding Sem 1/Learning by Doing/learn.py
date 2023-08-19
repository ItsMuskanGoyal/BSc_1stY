# s1 = "Welcome to Python"
# s2 = s1
# s3 = "Welcome to Python"
# s4 = "to"

# print(s1==s2)
# print(s2)
# print(s2.count('o'))
# print(len(s1))
# print(s2.count('o'))
# print(id(s1) == id(s2))
# print(id(s1) == id(s3))
# print(s1 <= s4)
# print(s2 >= s4)
# print(s1 != s4)
# print(s1.upper())
# print(s1.find(s4))
# print(s1[4],s1[4 : 8], 4 * s4, len(s1), max(s1))
# print(s1.startswith("o"))
# print(s1.isalpha())
# print(s1, s1)

# s=""
# print(len(s))

# s1 = "programming 101"
# s2 = "programming is fun"
# # s3= s1-s2
# # print(s3)          This will cause an error
# print(s1==s2)
# print(s1+s2)
# print(s1>=s2)
# print(len(s1), s1[0], s1[1:5], s2[ :5], s2[3: ])

# isequal= s1==s2
# print(isequal)
# print(s1[0:2]=="pr")
# x= len(s1)
# x1= s1[0]
# s3 =s1+" " +s2
# print(s3)
# x2=s1[1:4]
# print(x2)
# x4 = s1.upper()
# print(x4)
# x5 = s1.lower()
# print(x5)

# print(s1.replace("m","P"))
# print(s1)
# g=s1.find("e")
# print(g)
# h= s1.find("abc")
# print(h)


n= int(input("Enter the number of repetation"))
for i in range (n):
    print("Hello World")


# def character_frequency(string):
# # Create an empty dictionary to store character frequencies
# char_freq = {}

# # Iterate through each character in the string
# for char in string:
#     # If the character is not in the dictionary, add it and set the frequency to 1
#     if char not in char_freq:
#     char_freq[char] = 1
#     # If the character is already in the dictionary, increment the frequency by 1
#     else:
#     char_freq[char] += 1

# Iterate through the dictionary and print the frequency of each character
# for char, frequency in char_freq.items():
#     print("'{}' occurs {} times".format(char, frequency))



# def main():
# # Read the string from the user
#     string = input("Enter a string: ")

# # Call the character_frequency function
#     character_frequency(string)

if __name__ == '__main__':
    main()














height=int(input("Enter height of rectangle"))
width=int(input("Enter width of rectangle"))
area=height*width
print("area is: ", area)

side=int(input("Enter side of square:"))
areasq=side*side
print("Area of square is : ", areasq)

heighttri=int(input("Enter height of triangle"))
base=int(input("Enter base of triangle"))
areatri= 0.5*heighttri*base
print("Area is: ", areatri)


height = int(input("Enter the height of the triangle : "))

for i in range(height,0,-1):
        print(i* ' ' + (height+1-i) * '* ')

for i in range(1,11):
    print(i)



rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Rectangle Star Pattern")
i = 0
while(i < rows):
    j = 0
    while(j < columns):
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()


b= int(input("Enter the number"))
i=0
while(i<b):
    print(i)
    i=i+1




















# length=int(input("Enter the length of rectangle"))
# breadth=int(input("Enter the breadth of rectangle"))
# for i in range (0,length,+1):
#     print("*", end=' ')
#     for j in range (0,breadth,+1):
#         print("*")
#     print()


# for i in range(100):
#    print(i)

# def Fibonacci(n):
#     if n<= 0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

# print(Fibonacci(18))




# total = 0
# #your code goes here
# passengers=0
# while passengers<5:
#     passengers+=1
#     age=int(input())
#     for age in range <3:
#         continue
#     total+=1
#     print(total)

# ticket=0
# for i in range (5):
#         age= int(input("Enter the age"))
#         if(age>3):
#             ticket= ticket + 100
#             i=i+1
#         else:
#             ticket=ticket
#             i=i+1

# print(ticket)



# colors = ["voilet", "indigo", "blue"]
# colors.insert(2,"hi")
# colors.insert(2,"hiu")
# colors.insert(2,"hik")
# #colors.append("green")
# print(colors)


# for i in range(20, 41):
#     print(i)

# i=0
# for x in range(1,3):
#     j=0
#     for y in range(-2,0):
#         j=j+y
#         i=i+j
# print(i)



class Circle:
    def __init__(self, radius=1):
        self.radius = radius
        

    def getPerimeter(self):
        return 2 * self.radius * 3.14
    
    def getArea(self):
        return self.radius *self.radius * 3.14
    

c1 = Circle(21)
print(c1.getPerimeter())
print(Circle(35).getArea())



class Rectangle:
    #this is a class
    def __init__(self,l, w):
        self.l = l
        self.w= w
        #instance variable of object

    def getar(self):
        return self.l * self.w
    

print(Rectangle(10,20).getar())






# for i in range(5):
#     todo=["aa","bb"]
#     todo.append(input("Enter todo"))
#     print(todo)
