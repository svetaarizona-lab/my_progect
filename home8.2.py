#написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
#Паліндромом - це такий рядок, який читається однаково зліва направо і зправа
# наліво без урахування знаків пунктуації та розмірності букв.
#Функція приймає на вхід рядок, та повертає булеве значення True або False

def is_palindrome(text):
    #text = text.replace(' ','')
    #text = text.lower()
    cleaned = ''.join(x.lower() for x in text if x.isalnum())
    return cleaned == cleaned[::-1]
print(is_palindrome ("A man, a plan, a canal: Panama ")) #True remove sings
print (is_palindrome ("OP")) #False
print (is_palindrome ("a."))  #True
print (is_palindrome ("aurora"))#False
print ("OK")
