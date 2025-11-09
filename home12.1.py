import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
    Видаляє всі HTML-теги з файлу html_file
    і записує очищений текст у result_file.
    """
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = re.sub(r'<.*?>', '', html)

    text = re.sub(r'\s+', ' ', text)

    text = text.strip()

    with codecs.open(result_file, 'w', 'utf-8') as cleaned_file:
        cleaned_file.write(text)

    print(f"fail cleaned '{result_file}'")

delete_html_tags('draft.html')