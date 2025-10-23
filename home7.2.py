#На вхід функції correct_sentence передається речення.
# Необхідно повернути його виправлену копію так, щоб воно завжди починалося з
# великої літери та закінчувалося крапкою.
def correct_sentence(text):
    text = text.strip()
    if not text:
        return "."
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')