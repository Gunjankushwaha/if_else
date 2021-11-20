


print("***** welcom to satebank *****")
bal=50000
language=input("enter the language : ")
if language=="english":
    pin=input("input enter the pin number : ")
    if pin=="2320" or "12345":
        password=input("enter the pasword : ")
        if password=="123456" or "9876":
            transaction=input("enter the transaction : ")
            if transaction=="withdrawal":
                account=input("enter the account")
                if account=="saving":
                    amount=int(input("enter the amount : "))
                    bal1=bal-amount
                    print("your bal is",bal1)
                    account=input("enter the transaction : ")
                elif account=="carreant":
                       amount=int(input("enter the amount : "))
                       bal2=bal-amount
                       print("you bal is",bal2)
                       transaction=input("enter the transaction : ")
            elif transaction=="did":
                account=input ("enter the account : ")
                if account=="saving": 
                   amount=int(input("enter the amount : "))
                   bal3=bal+amount
                   print("your bal is",bal3)
                   account=inpu("enter the account : ")
                elif account=="carreant":
                    amount=int(input("enter rhe amount : "))
                    bal4=bal+amount
                    print("your bal is",bal4)
                    transaction=input("enter the inq balance : ")
        elif transaction=="inq balance":
            pin=input("enter the pin number")
            if pin=="12345":
                account= input("enter the account")
                account=

                    

                        # elif transaction=="did you mean":
                #     account=int(input("enter the carrean : "))
                #     if account=="carreant":
                #         amount=int(input)("enter the amount")
                #         bal2==bal-amount
                #         print("your bal is",bal2)
                         
                    # amount=50000
                    # bal2=bal-amount
                    # print("your bal is",bal2)
                    # print("did you mean")
                    
                #   amount=input("enter the amount")
                #   if amount=="1000" or "2000":
                #     print("available amount") 
#                     if balance=="1000":
#                     print("nikala")
#                   if cash=="5000":   
#                      print("ha")
#                      if last== "transaction"
#                      print("4000")
#                      else:
#                         print("atm mashin off kiya")
#                   else:
#                      print("kiya")
#                else:
#                   print("balance nikala")
#             else:
#                print("type kiya")
#          else:
#             print("salact hu")
#       else:
#          print("yestate s")
#    else:
#        print("correct language")





# print("***** welcom to atm *****")
# atm_name=input("enter the atm_name")
# if atm_name=="debit" and "credit":
# #     print("debit:")
#     language=("select the language")
#     if language=="english" and "hindi":
#         print("english")
#         pin_cod=input("enter the pin_cod")
#         if pin_cod=="5678":
#             print("it is right pin_cod")
#             password=input("enter the password")
#             if password=="gunjan@12345":
#                 print("so password")
#                 transaction=input("enter the transaction")
#                 if transaction=="take" or "give":
#                     print("take")
#                     account=input("chos the account")
#                     if account=="saving account" or "curreant account":
#                         print("saving account")
#                         amount=input("enter thr amount")
#                         if amount>="7000" or "another":
#                             print("it is tight another")
#                         else:
#                             print("available")
#                     else:
#                         print("good account")
#                 else:
#                     print("igive") 
#             else: 
#                 print("right password")
#         else:
#             print("select cod")
#     else:
#         print("it is right language")
# else:
#     print("right atm name")