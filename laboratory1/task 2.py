import re
"""
13) Визначити правильність дати, введеної з клавіатури (число - від 1 до 31, місяць - від 1 до 12.  Якщо введені некоректні дані, то повідомити про це.
"""
print("Надь Юлія Артурівна \nЛабораторна робота №1 \nВаріант 13 \nВизначення правильності дати\n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
re_inp=re.compile("\s{0,}[+]?\d{0,2}\s{0,}$")

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(text.match(pattern))

def day_inp(): # func for day input
    day = input("Enter the day(from 1 to 31): ")
    if validation(re_inp, day):
        day=int(day)
    else:
        print("Input is incorrect. Try again.")
        day_inp()
    return day

day = day_inp()

def month_inp():# func for month input
    month = input("Enter the month(from 1 to 12): ")
    if validation(re_inp, month):
        month = int(month)
    else:
        print("Input is incorrect. Try again.")
        month_inp()
    return month

month=month_inp()

def ans():
    answer=input("Do you want to continue(y/n)?")
    while validation(re_answy, answer)==False and validation(re_answn, answer)== False:
        print("You entered incorrect symbol, choose y or n")
        answer = input("Do you want to continue(y/n)?")
    if validation(re_answy, answer):
        day = day_inp()
        month = month_inp()
        cor_date(month, day)
    elif validation(re_answn, answer):
        print("Bye")
def cor_date(month, day):
    if month>12 or month<1 or day>31 or day<1:
        print("The date is not correct")
        ans()
    if month==1 or  month== 3 or  month==5 or  month==7 or  month==8 or  month==10 or  month==12:
        if 1<=day<=31:
            print("It's a correct date")
            ans()
        else:
            print("The date is not correct")
            ans()
    if month==4 or  month==6 or  month==9 or  month==11:
        if 1<=day<=30:
            print("It's a correct date")
            ans()
        else:
            print("The date is not correct")
            ans()
    if month==2:
        if 1<=day<=29:
            print("It's a correct date")
            ans()
        else:
            print("The date is not correct")
            ans()

cor_date(month, day)


