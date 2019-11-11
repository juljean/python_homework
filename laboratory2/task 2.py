import re
print("Надь Юлія Артурівна \nЛабораторна робота №2 \nВаріант 13 \nДано ціле число N(>0). Якщо воно є ступенем числа 3, то вивести True,\nякщо ні - вивести False.\n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
inp_n=re.compile("\s{0,}[+]?\d{0,}\s{0,}$")#index,int

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(text.match(pattern))

def val_power():
    power=input("Enter what power you want to check(only integers):")
    if validation(inp_n, power):
        power=int(power)
    else:
        print("You entered incorrect input. Try again.")
        val_power()
    return power
number=val_power()

def index():
    n=input("Enter the integer value n, that >=1:")
    if validation(inp_n, n):
        n=int(n)
        if n<1:
            print("You entered a wrong symbol. Try again.")
            index()
    else:
        print("You entered incorrect input. Try again.")
        index()
    return n
n=index()

def ans():
    answer=input("Do you want to continue(y/n)?")
    while validation(re_answy, answer) == False and validation(re_answn, answer) == False:
        print("You entered incorrect symbol, choose y or n")
        answer = input("Do you want to continue(y/n)?")
    if validation(re_answy, answer):
        val_power()
        index()
        eval(n, number)
    elif validation(re_answn, answer):
        print("Bye")

def eval(n, number):
    while n>1:
        n=n/number
    if n==1:
        print("True")
        ans()
    else:
        print("False")
        ans()

eval(n, number)