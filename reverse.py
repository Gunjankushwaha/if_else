num=int(input("enter the reverse number"))
# a= num%10
# b=(num//10)%10
# c=(num//100)%10
# d=(num//100)%10
# numnwe=(a*100)+(b*10)+(c*10)+(d*10)
a=num%10
b=(num%10)//10
c=(num//10)//10
d=a+b+c
if num%d==0:
   print(num)
else:
    print(num,"reverse number")
    


# num=int (input("enter reverse number"))
# a= (num%10)
# b= (num//10)%10
# if num<=100:
#     print("reverse number")
# else:
#     print("not reverse number")    