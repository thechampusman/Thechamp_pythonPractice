year = int(input("Enter a year : "))

if year % 100 == 0 :
    if year %  400 == 0:
        print ("Leap Year ")
        
    else:
        print("Not A Leap Year")

elif  year % 4 == 0 :
    print("Leap Year")

else: print("Not A Leap Year")