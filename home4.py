print("Welcome to the system!")

user_gmail = str(input("Введіть вашу електронну адресу: "))
char_gmail = []

# Проверка на пустую строку
if not user_gmail:
    print("Помилка: ви нічого не ввели.")
else:
    if "@" not in user_gmail or "." not in user_gmail:
        print("Помилка: введіть правильну електронну адресу.")

    else:
            number_interactions = 0
            for char in user_gmail:
                number_interactions += 1
                if "@" not in char_gmail:
                    char_gmail.append(char)
            char_gmail.remove("@")

            interactions_secret = 0
            for char_secret in char_gmail[1:-1]:
                interactions_secret += 1
                char_secret = "*"
                char_gmail[interactions_secret] = char_secret

            print("Ваша електронна адреса:", "".join(char_gmail) + "@" + ".com")