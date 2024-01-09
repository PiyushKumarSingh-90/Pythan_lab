a=int(input("\n\nEntery timeing : "))
b=int(input("exit timeing : "))
c=b-a



if(c <= 3) :
    p=int(input("\nEnter the car type: \n1.CAR \n2.BUS \n3.BICK : \n"))
    
    if(p==1):
        print("\nTYPE |  UP TO 3 HOUR  | MORE THEN 3 HOUR ")
        
        print(" Car  |      10        |      20")
        print(F"\nU PARK YOUR VEHICAL FOR {c} HOURS. SO, U HAVE TO PAY : RS.",c*10)
        
    elif(p==2):
        print("\nTYPE |  UP TO 3 HOUR  | MORE THEN 3 HOUR ")
        
        print(" Bus |      20        |      30")
        print(F"\nU PARK YOUR VEHICAL FOR {c} HOURS. SO, U HAVE TO PAY : RS.",c*20)
    
    elif(p==3):
        print("\nTYPE |  UP TO 3 HOUR  | MORE THEN 3 HOUR ")
        
        print("Bick |      5         |      10")
        print(F"\nU PARK YOUR VEHICAL FOR {c} HOURS. SO, U HAVE TO PAY : RS.",c*5)


elif(c >= 3) :
    p=int(input("\nEnter the car type: \n1.CAR \n2.BUS \n3.BICK : \n"))
    
    if(p==1):
        print("\nTYPE |  UP TO 3 HOUR  | MORE THEN 3 HOUR ")
        
        print(" Car  |      10        |      20")
        print(F"\nU PARK YOUR VEHICAL FOR {c} HOURS. SO, U HAVE TO PAY : RS.",(c*20)-30)
        
    elif(p==2):
        print("\nTYPE |  UP TO 3 HOUR  | MORE THEN 3 HOUR ")
        
        print(" Bus |      20        |      30")
        print(F"\nU PARK YOUR VEHICAL FOR {c} HOURS. SO, U HAVE TO PAY : RS.",((c*30)-60)+30)
    
    elif(p==3):
        print("\nTYPE |  UP TO 3 HOUR  | MORE THEN 3 HOUR ")

        print("Bick |      5         |      10")
        print(F"\nU PARK YOUR VEHICAL FOR {c} HOURS. SO, U HAVE TO PAY : RS.",(c*10)-15)        



