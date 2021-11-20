day=input("enter the day:")
if day=="monday":
    disco=input("disco se parmition mila:") 
    if disco=="ha":
        vaccinated=input("vaccinated ho ya nahi:")
        if vaccinated=="ha":
            print("not quarrantine")
        else:
            print("quarrantine")
    else:
        print("not parmition hai")
else:
    print("bahar jana hai")                