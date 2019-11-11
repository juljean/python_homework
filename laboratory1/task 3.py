import re
"""
при х>3, y=-3x+9
при х<=3, y=x^3/(x^2+8)
"""
print("Надь Юлія Артурівна \nЛабораторна робота №1 \nВаріант 13 \nЗнаходження усіх значень функції \n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
re_inp=re.compile("\s{0,}[+-]?\d{0,}\s{0,}$")

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(text.match(pattern))

def inp_val():
    val=input("Enter the value you want to calculate:")
    if validation(re_inp, val):
        val=int(val)
    else:
        print("You entered incorrect input. Try again.")
        inp_val()
    return val

val=inp_val()

def ans():
    answer=input("Do you want to continue(y/n)?")
    while validation(re_answy, answer)==False and validation(re_answn, answer)== False:
        print("You entered incorrect symbol, choose y or n")
        answer = input("Do you want to continue(y/n)?")
    if validation(re_answy, answer):
        val = inp_val()
        eval_func(val)
    elif validation(re_answn, answer):
        print("Bye")

def eval_func(val):
    if val>3:
        newval=val*(-3)+9
        print(newval)
        ans()
    else:
        newval=(val**3)/((val**2)+8)
        print(newval)
        ans()

eval_func(val)