
corrent_location=["katraj","tulshi bag","shivaji nahar"]
dropping_point=["shivapur","taur plaza","swarget"]
driver_name=["sonu","deepak","vivek"]
van_colour=["red","yellow","whiet"]
van_no=[3,4,5]

i=0
while i<len(corrent_location[i]):
    user=input("enter the location")
    if user==corrent_location[i]:
        print("now avileble")
        user1=input("enter tha droppin_point")
        if user1==dropping_point[i]:
            print("avilebal")
            name=input("enter the name")
            if name==driver_name[i]:
                print("comeing now")
    else:
        print("not avilebal")
i=i+1