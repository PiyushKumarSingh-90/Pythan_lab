#                                   cube root

# import math

# def cuberoot(a):
#     return math.cbrt(a)

# int=cuberoot(3.8)
# print(int)


#                          how to use [*ards]



# EX:-1

# def my_function(*args):
#     for i in args:
#         print(i,end=",")

# my_function(3)
# my_function(3,4)
# my_function('Piyush',18, 'M')



# def my_function(a):
#     print(a)
# my_function(5 * 3 + 4) 




# EX:-2

# def sum_lst(*l):
#     sum = 0
#     for i in l[0]: 
#         sum += i 

#     return sum
# # return sum(argh)

# n=int(input("\n\nEnter how many no. u want : "))
# l=[]


# for i in range(0,n):
#     a = int(input(f"Ente the {i+1} no. : "))
#     l.append(a)

# print(f"\nTotal sum is : {sum_lst(l)}")



#                          use of [**kwargs]


#  EX:-1

# def my_funciton(*args,**kwargs):
#     # print(args)
#     print(kwargs)
#     print(args)

# my_funciton("hello",'ITM',name='piyush k. singh',age=20,gender='M')


# # EX:-2

# def my_function(kwargs):
#     print(f"WELCOME {kwargs} TO ITM")


# my_function("piyush") 


# EX:-3 

# def details(**kwargs):
#     print("\n")
#     for i in kwargs:

#         print (i,kwargs[i])

# l=[]

# print("\n\nEnter your details : ")
# n=input("\nEnter your name : ")
# r=input("Enter your roll no.  : ")
# l.append(r)

# ag=input("Enter your age : ")
# em=input("Enter your Email : ")

# details(name=n,roll_no=r,age=ag,email=em)




# var_global = 4

# def func():
#     var_global = 3
#     print (var_global) 

# func()
# print(var_global) 

def main():
    a=10
    b=55
    print("int function main......dir()=",dir())
    result = absdiff(a,b)
    print("the absulate value of",a,"-",b,"=",result)

def absdiff(x,y):
    print("int function main......dir()=",dir())
    if x>y:
        z=x-y
    else:
        z=y-x
    return z  

main()      
