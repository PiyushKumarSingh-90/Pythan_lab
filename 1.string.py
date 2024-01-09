str='ITM SKILL UNIVERSITY'

# print(str[0:4])
# print(str[0:])
# print(str[-4:-1])
# print(str[:-1])
# print(str[4:9])
# print(str[0::1])
# print(str[0::2])
# print(str[::-1])


# for i in str:
#     print(i)


# i=0
# while(i<len(str)):
#     print(str[i])
#     i+=1


def fun(str,char):

    
    for i in range(len(str)):
        ele = str[i]
        if ele==char:
            a = i
            print(a)

str=input("Enter the string : ")
char=input("Enter the char : ")

fun(str,char)










