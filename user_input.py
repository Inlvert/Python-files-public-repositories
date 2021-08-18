def reverse(text):
    return text[::-1]
def is_palindrom(text):
    return text == reverse(text)
something = input('Введите текст:')
if (is_palindrom(something)):
    print("Да, это палиндром")
else:
    print("Нет это не палиндром")