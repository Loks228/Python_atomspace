print("Welcome to the system!")

full_name = input("Введіть ім'я та прізвище: ")
full_name = full_name.strip()

# Проверка на пустую строку
if not full_name:
    print("Помилка: ви нічого не ввели.")
else:
    parts = full_name.split()
    
    # Проверка, что есть минимум имя и фамилия
    if len(parts) < 2:
        print("Помилка: введіть ім'я та прізвище.")
    else:
        first_name = parts[0]
        last_name = parts[1]
        
        initials = first_name[0].upper() + "." + last_name[0].upper() + "."
        
        print("Ваші ініціали:", initials)