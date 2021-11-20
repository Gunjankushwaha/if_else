print("welcom to facebook")
facebook_name=input("enter the name")
if facebook_name=="gunjan"or"sona":
    print("correct your name")
    full_name=input("enter the full_name:")
    if full_name=="gunjan kushwaha" or "sona kumari":
        print("correct name")
        password=input("enter the password:")
        if password=="567893":
            print("good password")
            gmail=input("enter the gmail")
            if gmail=="gunjankushwahakumari":
                print("right gmail")
                gender=input("enter the gender")
                if gender=="male" or "female":
                    print("ok")
                    birthday=input("enter the dade of birth")
                    if birthday>="0 to 9":
                        print("dade birth is right")
                    else:
                        print("wrong your dade birth")
                else:
                    print("wrong")
            else:
                print("wrong your gmail")
        else:
            print("wrong your password")
    else:
        print("wrong your full_name")
else:
    print("wrong your name")    