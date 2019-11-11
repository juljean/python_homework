import re
"""
"""
print("Надь Юлія Артурівна \nЛабораторна робота №3 \nВаріант 13 \nВставити пробіл перед останніми 2-ма символами \nв слова, що мають мінімальну (задану) довжину.\n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
digitals=re.compile("\s{0,}[0-9]*\.?[0-9]*\s{0,}$")#int

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(text.match(pattern))

def word_length(): #insert minimal length of the word
    length=input("Enter the minimal length of the word:")
    if validation(digitals,length):
        if length == "" or length == " ":
            print("You entered incorrect symbol.Try again(only digitals)")
            word_length()
        else:
            length=int(length)
    else:
        print("You entered incorrect symbol.Try again(only digitals)")
        word_length()
    return length

length=word_length()
def symbols_num(): #amount of symbols
    ams=input("Enter from how many symbols from the end you want to apply changes(print number: 2 means the second from the end):")
    if validation(digitals,ams):
        if ams == "" or ams == " ":
            print("You entered incorrect symbol.Try again(only digitals)")
            symbols_num()
        else:
            ams=int(ams)
            if ams>length:
                print("It's to big value. Try again.")
                symbols_num()
    else:
        print("You entered incorrect symbol.Try again(only digitals)")
        symbols_num()
    return ams
def sym_change(): #changes like ** within the text
    change = input("Enter what symbols you want to insert as changes:")
    return change

ams=symbols_num()
change=sym_change()

def ans():
    answer=input("Do you want to continue(y/n)?")
    if validation(re_answy, answer):
        length = word_length()
        ams = symbols_num()
        change = sym_change()
        main_func(length, ams, change)
    elif validation(re_answn, answer):
        print("Bye")
    else:
        print("You entered incorrect symbol, choose y or n")
        ans()
def main_func(length, ams, change):
    """
    Функція приймає значення мінімальної довжини слова типу int , при якій будуть зміни, положення зміни у слові типу int,
    та саму зміну типу str. Вертає вже змінене слово.
    :param length: int
    :param ams: int
    :param change: str
    :return: str
    """
    word= input("Enter the word:")
    if len(word)<length:
        print("The word is too short. Try again.")
        main_func(length, ams, change)
    elif len(word)==length:
            print(word[:length-ams]+ change +word[length-ams:])
    else:
        print(word)
    ans()
main_func(length, ams, change)