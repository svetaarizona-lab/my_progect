#Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
import keyword
import string

name = input("Please:  enter the line : ")

if (
        not name #пустий рядок
        or name[0].isdigit() #не з цифри
        or any(ch.isupper() for ch in name) # не великі літери
        or any(ch in string.punctuation.replace('_', '') for ch in name) #заборона знаків пунктуації
        or ' ' in name # пробіли заборонені
        or name.count('_') > 1
        or name in keyword.kwlist
):
    print(False)
else:
    print(True)
