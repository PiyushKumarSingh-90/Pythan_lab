cart=[]

print("")

print("____________________________WELCOME TO THE LIBRARY______________________________")

print("\n","WE HAVE THIS KIND OF BOOK :- ")

print("\n","1.Horror","\n","2.Love Story","\n","3.Novel","\n","4.Autobiography","\n",)



choice=int(input("Which book do u want from this: "))

if choice ==1 : 
    print("\n                 WE HAVE THIS KIND OF HORROR BOOKS")
    print("")
    print("\n","1.ANNA BELLA ","\n","2.CONJURING","\n","3.EXOSTISTS")
    
    choice1=int(input("\nWhich book do u want form this : "))
    
    if choice1==1:
        cart.append('ANNA BELLA')

    elif choice1==2: 
        cart.append('CONJURING')   

    elif  choice1==3: 
        cart.append('EXOSTISTS')

    else:
        print("INVALID INPUT")

elif choice == 2 : 
    print("\n                 WE HAVE THIS KIND OF Love Story BOOKS")
    print("")
    print("\n","1.ANNA BELLA","\n","2.CONJURING ","\n","3.EXOSTISTS")

    choice1=int(input("\nWhich book do u want form this : "))
    
    if choice1==1:
        cart.append('ANNA BELLA')

    elif choice1==2: 
        cart.append('CONJURING') 

    elif  choice1==3: 
        cart.append('EXOSTISTS') 
    else:
        print("INVALID INPUT")

elif choice == 3 : 
    print("\n                 WE HAVE THIS KIND OF Novel BOOKS")
    print("")
    print("\n","1.BELIEVE IN YOURSELF","\n","2.YOU CAN","\n","3.BELOVED")

    choice1=int(input("\nWhich book do u want form this : "))
    
    if choice1==1:
        cart.append('BELIEVE IN YOURSELF')

    elif choice1==2: 
        cart.append('YOU CAN')  

    elif  choice1==3: 
        cart.append('BELOVED')

    else:
        print("INVALID INPUT")

elif choice == 4 : 
    print("\n                 WE HAVE THIS KIND OF Autobiography BOOKS")
    print("")
    
    print("\n","1.WONGS OF FIRE","\n","2.MY INVANTION","\n","3.THE STORY OF MY")

    choice1=int(input("\nWhich book do u want form this : "))
    
    if choice1==1:
        cart.append('WONGS OF FIRE')

    elif choice1==2: 
        cart.append('MY INVANTION')  

    elif  choice1==3: 
        cart.append('THE STORY OF MY')  

    else:
        print("INVALID INPUT") 


else : 
    print("INVALID CHOICE")

print("\n\n                        YOUR CART DETAILS :- ")
print("\n",cart)


