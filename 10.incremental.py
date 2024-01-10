import math

# def  dist(x1,x2,y1,y2):
#     z=((abs(x2-x1))*(abs(x2-x1)))+((abs(y2-y1))*(abs(y2-y1)))
#     return z

# a=dist(2,4,3,5)
# print(math.sqrt(a))



def area(x1,y1,x2,y2):
    c=(abs(x2-x1)*abs(x2-x1))+(abs(y2-y1)*abs(y2-y1))
    return c

x1=int(input("\n\nEnter the cente x-axis of a circle : ") )
y1=int(input("Enter the center y-axis of a circle : "))
x2=int(input("Enter the edge x-axis of a circle : "))
y2=int(input("Enter the edge y-axis of a circle : "))

a = area(x1,y1,x2,y2)
r=math.sqrt(a)
print(f"Area is : {3.14*r*r}")
