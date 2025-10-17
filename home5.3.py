#Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
import string

text = input("Please:  enter the line : ").strip()
for ch in string.punctuation:
    text = text.replace(ch, ' ') #замінюємо на пробіли

words = text.split() #видаляємо зайві пробіли
if not words:
    print(False)
else:
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    if len(hashtag) > 140:
        print(False)
    else:
        print(hashtag)