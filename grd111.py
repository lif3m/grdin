
import keyboard

escape=keyboard.is_pressed('esc')
found=keyboard.is_pressed('ctrl+f')
append=keyboard.is_pressed('plus')

dictionary = { "яблоко": {"apple", "pome"}, "банан": {"banana"}, "груша": {"pear"}, "апельсин": {"orange"}, "киви": {"kiwi"}, }

print("-" * 100)

while True:
    print('Список возможных действий:')
    print('1 - Для поиска слова с ловаре нажмите ctrl+f')
    print('2 - Для добавления слова в с словарь нажмите +')
    print('3 - Нажмите esc для выхода')
    print("-" * 100)

    if keyboard.is_pressed('ctrl+f'):
        hide_word=input("Введите слово: ")
        if hide_word in dictionary:
            print(dictionary[hide_word])
            print("-"*100)

    if keyboard.is_pressed('plus'):
        new_word=input("Введите новое слово: ")
        dictionary[new_word]


    if keyboard.is_pressed('esc'):
        print("Досвидания!!!")
        break


