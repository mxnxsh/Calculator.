
def calc_add():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a+b
    return c

def calc_sub():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a-b
    return c

def calc_float_div():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b
    return c

def calc_int_div():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a//b
    return c

def calc_multi():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a*b
    return c

def calc_square():
    a=int(input("enter a number"))
    c=a*a
    return c
while True:
    print("\n1 = addition \n2 = subtraction \n3 = float division \n"
          "4 = intiger division \n5 = multiply \n6 = square \n"
          "7 = to change Calculator")

    choice=int(input("enter your choice="))

    if(choice==1):
        print("the addition of above two numbers =",calc_add())

    elif(choice==2):
        print("the subtraction of above two numbers =",calc_sub())

    elif(choice==3):
        print("the float division of above two numbers =",calc_float_div())

    elif(choice==4):
        print("the intiger division of above two numbers =",calc_int_div())

    elif(choice==5):
        print("the multiplication of above two numbers =",calc_multi())

    elif(choice==6):
        print("the square of above number is =",calc_square())

    elif(choice==7):
        import _direct

    elif(choice==0): break

    else:
        print("sorry you selected a choice which is not mention")
