import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
    очистить текст від html-тегів і запише цей текст в інший файл
    видалити ці символи та все, що між ними
    Функція отримує на вхід два параметри – ім'я файлу, та куди записати
    """
    with codecs.open(html_file, 'r', 'utf-8') as file: #r-reading
        html = file.read()

    text = ""   #delete
    inside_tag = False

    for ch in html:
        if ch == '<':
            inside_tag = True
        elif ch == '>':
            inside_tag = False
        elif not inside_tag:
            text += ch

    text = " ".join(text.split()) #extra spaces

    with codecs.open(result_file, 'w', 'utf-8') as cleaned_file: #record fail
        cleaned_file.write(text.strip())

    print(f"Fail cleans and saved in  '{result_file}'") #new resalt

delete_html_tags('draft.html')