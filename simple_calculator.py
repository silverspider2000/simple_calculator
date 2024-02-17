#silverspider      follow me
#https://github.com/silverspider2000
#www.linkedin.com/in/seyed-ali-mousavi-silverspider
#telegram: t.me/silverspider_official
#gmail: silverspider.official@gmail.com
def again():
        calc_again =input("reset app ?(y/n) :")
        if calc_again == "y" :
            calculate()
        elif calc_again == "n" :
            exit
        else :
            again()

def calculate():
    operation = input("please choose operation:/n + , - , * , /    :")
    number1=int(input("number 1 : "))
    number2=int(input("number 2 : "))
    if operation=="+":
        print("{} + {} = ".format(number1,number2))
        print(number1+number2)
    elif operation=="-":
        print("{} - {} = ".format(number1,number2))
        print(number1-number2)
    elif operation=="*":
        print("{} * {} = ".format(number1,number2))
        print(number1*number2)
    elif operation=="/":
        print("{} / {} = ".format(number1,number2))
        print(number1/number2)
    else:
        print("operation is not exist")
        again()
    
        
calculate()
        

