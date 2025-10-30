#На вхід функції popular_words передаються два аргументи. Текст та список слів,
# популярність яких необхідно визначити.
def popular_words(text: str, words: list):
   text_words = text.lower().split()
   result = {}
   for word in words:
       result[word] = text_words.count(word)
   return result

text = "When I was One I had just begun When I was Two I was nearly new"
words = ['i', 'was', 'three', 'near']

result = popular_words(text, words)
print(result)
print("OK")