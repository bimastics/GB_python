# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Введите данные: ').split(' ')

for num, word in enumerate(string, start=1):
    print(f'{num}. {word[:10]}')