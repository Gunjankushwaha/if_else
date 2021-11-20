
import json
from pprint import pprint
print("...../n WELCOME TO OLA")

corrent_location=["khedshivapur","toalplaza","swarget","khopi"]
dropping_point=["katraj","tulisibagh","shivaji nager","dmart"]
driver_name=["vikky","vivek","sonu","vikash"]
ola_colour=["red","yellow","black","pink"]
rating=[1,2,5,3,8,5]
van_no=["MH 2349","AN 1921","UP 4567","TCL 3921"]
feedback=["Good ","comunition is not good","he is good drive","amezing"]
list=[]
index=0
for i in range(len(driver_name)):
    index=index+1
    corrent_location1=corrent_location[i]
    dropping_point1=dropping_point[i]
    driver_name1=driver_name[i]
    ola_colour1=ola_colour[i]
    rating1=rating[i]
    van_no1=van_no[i]
    feedback1=feedback[i]
    new_list={"corrent_location":corrent_location,"dropping_point":dropping_point,"driver_name":driver_name,"ola_colour":ola_colour,"rating":rating,"van_no":van_no,"feedback":feedback}
    list.append(new_list)
with open("data_ola.json","w")as file:
    json.dump(list,file,indent=4)
    pprint(list)
# print()
# print("....ola persent driver")
# location=input("enter the location")
# if location=="khedshivapur" or location=="taorplaza" or locatino=="swarget" or location=="khopi":
#     print(location)
#     dropping=input("enter the dropping_point")
#     if dropping_point=="katraj" or dropping_point=="tulsibag" or dropping_point=="shivaji nagar" or dropping_point=="dmart":
#         print(dropping)
#     else:
#         print("sorry your ola is nat availeble")
# else:
#     print("your ola is not avileble now")




