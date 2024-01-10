#                          globel,non local ,and local vairable


# var1=10    #Global Veriable

# def fun():
    
#     var1=3
#     print(var1)
    
#     def fun2():
#         nonlocal var1
#         var1=4
#         print(var1)


#     fun2()
#     print(var1) 

# fun()
# print(var1)        


# def func1(b):
#     b = 10
#     print(b)
#     global a
#     a = b 
#     print(a)
#     def func2():
#         b = 21
#         print(b)
#     print(b)
#     func2()
#     print(b)
    
    
# a = 11 

# func1(a)
# print(a)


a = 10
def fun(b):
    print(b)
    global a
    c = a
    a += b
    print(a)
    b = 10
    print(b)
    def fun1():
        nonlocal c
        global a
        print(c)
        print(a)
        d = a+c
        print(d)
    def fun2():
        global a
        print(a)
        d = 0
        print(d)
        nonlocal c
        print(c)
    print(c)
    fun1()
    fun2()
    print(c)
    
        

fun(a)
print(a)