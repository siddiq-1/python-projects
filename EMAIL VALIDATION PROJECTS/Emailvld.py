from curses.ascii import isspace


email= input("Enter your Email: ") 
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="." or i== "@":
                        print("Right email")
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong email make sure you enter the correct email")
            else:
                print("Wrong email make sure you write the email correctly check your dot")
        else:
            print("Wrong email make sure that @ is use and at once")
    else:
        print("Wrong email make sure you start your email with Alphabet")
else:
    print("Wrong email character should be minimum 6")