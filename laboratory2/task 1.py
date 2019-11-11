import re
print("Надь Юлія Артурівна \nЛабораторна робота №2 \nВаріант 13 \nОбчислення значення по формулі.\n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
inp_x=re.compile("\s{0,}[-+]?[0-9]*\.?[0-9]*\s{0,}$")#float +-
inp_int=re.compile("\s{0,}[+]?\d{0,}\s{0,}$")#index,int

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(text.match(pattern))

def index():
    n=input("Enter the integer value n, that >=1:")
    if validation(inp_int, n):
        n=int(n)
        if n<1:
            print("You entered a wrong symbol. Try again.")
            index()
    else:
        print("You entered incorrect input. Try again.")
        index()
    return n
n= index()

def val():
    x=input("Enter the value x:")
    if validation(inp_x, x):
        x=float(x)
    else:
        print("You entered incorrect input. Try again.")
        val()
    return x
x=val()

def val_power():
    power=input("Enter the power you want to apply to the equation(only integers):")
    if validation(inp_int, power):
        power=int(power)
    else:
        print("You entered incorrect input. Try again.")
        val_power()
    return power
power= val_power()

def ans():
    answer=input("Do you want to continue(y/n)?")
    while validation(re_answy, answer) == False and validation(re_answn, answer) == False:
        print("You entered incorrect symbol, choose y or n")
        answer = input("Do you want to continue(y/n)?")
    if validation(re_answy, answer):
        index()
        val()
        val_power()
        eval(x, n,power)
    elif validation(re_answn, answer):
        print("Bye")

def eval(x,n, power):
    result=0
    for element in range (1,n+1):
        stage=(x+element)**power
        result+=stage
    print(result)
    ans()

eval(x, n, power)
