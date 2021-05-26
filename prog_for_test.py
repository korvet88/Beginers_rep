import random
def generate_password(l_n, chars):
    rez = ""
    for i in range(l_n - 1):
        a = random.randint(0, len(chars))
        rez += chars[a]
    return rez

def delete_str_element(del_chr, char_line):
    char_rez = ""
    for i in range(len(char_line)):
        for j in range(len(del_chr)):
            if char_line[i] not in del_chr:
                char_rez += char_line[i]
    return char_rez


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""
print("How are you")
print("Сколько паролей:")
n = int(input())
print("Задать длину пароля:")
l_n = int(input())
print("Включать ли цифры 0123456789?, y/n")
digits_y = input()
if digits_y == "y":
    chars += digits
print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?, y/n")
uppercase_letters_y = input()
if uppercase_letters_y == "y":
    chars += uppercase_letters
print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?, y/n")
lowercase_letters_y = input()
if lowercase_letters_y == "y":
    chars += lowercase_letters
print("Включать ли символы !#$%&*+-=?@^_?, y/n")
punctuation_y = input()
if punctuation_y == "y":
    chars += punctuation
print("Исключать ли неоднозначные символы il1Lo0O ? , y/n")
non_perfekt_simbol = ""
non_perfekt_simbol_y = input()
if non_perfekt_simbol_y == "y":
    delete_str_element(non_perfekt_simbol, chars)
for i in range(n):
    print(generate_password(l_n, chars))

