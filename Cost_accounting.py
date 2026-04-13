# Калькулятор
# Ви розробляєте інтерактивний калькулятор.

# Користувач повинен мати можливість багаторазово виконувати операції, поки сам не вирішить завершити програму.

# Програма повинна:
# Запитати у користувача два числа.
# Запитати операцію (+, -, *, /, **).
# Виконати обрану операцію за допомогою if-else.
# Вивести результат.
# Якщо користувач ввів невірну операцію – вивести повідомлення про помилку.
# Після кожної операції знову запитувати нові дані.
# Додати можливість виходу з програми.
# Дозволяється будь-яке ключове слово або знак, який потрібно ввести для завершення програми.


def add_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
        
    return num1 + num2

def subtract_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
        
    return num1 - num2

def multiply_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    return num1 * num2

def divide_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    
    return round(num1 / num2)

while input("Ви хочете порахувати? (yes/no): ").lower() == 'yes': 
    print('Ви хочете add_numbers')        
    print('Ви хочете subtract_numbers')   
    print('Ви хочете multiply_numbers')  
    print('Ви хочете divide_numbers')
    print('Напиши метод, який хочеш виконати.')

    def_method = input("Введіть назву операції, яку хочете виконати: ").strip().lower()

    num1_user = int(input("Та напиши числo для виконання операції: "))
    num2_user = int(input("Та ще одне будь ласка напиши числo для виконання операції) : "))

    try:
        if def_method == "add_numbers":
            print(add_numbers(num1_user, num2_user))  # Output: 15
        elif def_method == "subtract_numbers":            
            print(subtract_numbers(num1_user, num2_user))  # Output: 5
        elif def_method == "multiply_numbers":            
            print(multiply_numbers(num1_user, num2_user))  # Output: 50
        elif def_method == "divide_numbers":            
            print(divide_numbers(num1_user, num2_user))  # Output: 2.0
        else:
            print("Невідома операція. Будь ласка, виберіть одну з наступних: add_numbers, subtract_numbers, multiply_numbers, divide_numbers.")


    except ValueError as e:
        print("Error:", e)  


balance = float(input("Введіть початковий баланс: "))
expenses = {}





# Облік витрат за категоріями
# Ви розробляєте просту систему обліку витрат.

# Користувач має початковий баланс і може додавати витрати за різними категоріями (наприклад: їжа, транспорт, розваги).

# Програма повинна:
# Запитати початковий баланс користувача.
# Зберігати баланс у змінній.
# Створити словник для збереження витрат за категоріями.
# У циклі запитувати:
# - категорію витрат
# (слідкуйте за форматуванням: категорії не повинні дублюватися через різний регістр — наприклад, “Їжа” та “їжа” мають вважатися однією категорією)
# - суму витрат
# Якщо після витрати баланс стає менше нуля - вивести повідомлення про помилку
# Якщо все коректно:
# - зменшити баланс
# - додати витрати у відповідну категорію
# Після кожної операції виводити:
# - поточний баланс
# - всі витрати за категоріями
# Додати можливість виходу з програми (наприклад, при введенні “вихід”).

while True:
    category = input("\nВведіть категорію витрат (або 'вихід'): ").strip().lower()
    
    if category == "вихід":
        print("Завершення програми.")
        break

    try:
        amount = float(input("Введіть суму витрат: "))
        
        if balance - amount < 0:
            print("Помилка: недостатньо коштів!")
            continue

        # зменшуємо баланс
        balance -= amount

        # додаємо витрати в категорію
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        # вивід результату
        print("\nПоточний баланс:", balance)
        print("Витрати за категоріями:")
        for cat, val in expenses.items():
            print(f"- {cat}: {val}")

    except ValueError:
        print("Помилка: введіть коректне число.")

