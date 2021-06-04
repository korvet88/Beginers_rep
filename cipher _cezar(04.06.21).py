
"""Получим набор данных о шифр/дешифр, язык, шаг, текст, """
counter = 0

while True:
    print("Введите операцию: s - для шифрования, d - для дешифрования")
    oper = input()
    if oper == "s" or oper == "d":
        counter = 0
        break
    else:
        counter += 1

    if counter == 5:
        print("Иди остынь и вводи верно!")
        exit(0)

while True:    
    print("Введите язык шифрования: rus - для русского языка, en - для английского языка")
    languadge = input()
    if (languadge == "rus") or (languadge == "en"):
        counter = 0
        break
    else:
        counter += 1
    if counter == 5:
        print("Иди остынь и вводи верно!")
        sys.exit()

while True:
    print("Введите сдвиг: left - сдвиг влево, rigth - сдвиг вправо")
    step_for = input()
    if step_for == "left" or step_for == "rigth":
        counter = 0
        break
    else:
        counter += 1
    if counter == 5:
        print("Иди остынь и вводи верно!")
        exit(0)
while True:
    """Fix me для разных яз."""
    print("Введите шаг числом от 0 до 33 для rus и от 0 до 22 для en:")
    step = int(input())
    if step >= 0 or step <34:
        counter = 0
        break
    else:
        counter += 1
    if counter == 5:
        print("Иди остынь и вводи верно!")
        exit(0)

print("Введите ваш текс, для проведения нужной опереции")
text = input()    
print("Вввод даннызх завершен")

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

out_text = []
if languadge == "rus":
    for i in text:
        if i in rus_upper_alphabet:
            rez = int(rus_upper_alphabet.find(i) + step%len(rus_upper_alphabet))
            out_text.append(rus_upper_alphabet(rez))
        if i in rus_lower_alphabet:
            rez = int(rus_lower_alphabet.find(i) + step%len(rus_lower_alphabet))
            out_text.append(rus_lower_alphabet(rez))
        else:
            out_text.append(i)
print(*out_text)





