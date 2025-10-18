#Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.

import string

text = input("Please:  enter the two letters with - : ")

start , end = text.split  ("-")
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)
if start_index > end_index:
    start_index,end_index = end_index,start_index
result = letters[start_index:end_index+1]
print(result)