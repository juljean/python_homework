import re
print("Надь Юлія Артурівна \nЛабораторна робота №1 \nВаріант 13 \nЗнаходження усіх чисел Армстронга у діапазоні від 1 до n \n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with answer yes
re_answn=re.compile("\s{0,}n\s{0,}$")#comparing with answer no
re_inp=re.compile("\s{0,}[+]?\d{0,}\s{0,}$")#comparing with int digitals
def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(text.match(pattern))
def inp_val():
    secind = input("Enter the range\nin what you want to check the amount of Armrsrong values\n(from 1 to n) : ")
    while validation(re_inp, secind) == False:
        print("You entered incorrect symbol, choose y or n")
        secind = input("Enter the range\nin what you want to check the amount of Armrsrong values\n(from 1 to n) : ")
    if validation(re_inp, secind):
        secind=int(secind)
        armstrong_eval()
        if secind<1:
          print("Incorrect input: print the number bigger or equal to 1")
          inp_val()
    return secind
def ans():
    answer=input("Do you want to continue(y/n)?")
    while validation(re_answy, answer)==False and validation(re_answn, answer)== False:
        print("You entered incorrect symbol, choose y or n")
        answer = input("Do you want to continue(y/n)?")
    if validation(re_answy, answer):
       armstrong_eval()
    elif validation(re_answn, answer):
        print("Bye")

def armstrong_eval():
    for num in range(1, inp_val() + 1):
      summ = 0
      temp_val = num
      pum=str(temp_val)#for len function
      length=len(pum)
      while temp_val > 0:
          digit = temp_val % 10
          summ += digit ** length#it's a definition of armstr.num: 153=1**3+5**3+3**3=1+125+27=153
          temp_val //= 10
      if num == summ:#check if it is the Armstrong value
         print(num)
    ans()
armstrong_eval()

