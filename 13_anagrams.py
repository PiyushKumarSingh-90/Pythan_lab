#  wap to check if two strings are anagrams of each other.

w1=input("Enter the first word : ")
w2=input("Enter the second word : ")

toggle = True

for i in w1:
    if w1.count(i) != w2.count(i): # { count() } function count the no. of repatating word in  senstance
        toggle = False
        break
    else:
        toggle = True
if (toggle == True):

    print("Yes")
else:
    print("not")

