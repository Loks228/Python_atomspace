# user_info = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }
# def greet(name):
    
#     print(f"Hello, {name}!")
# greet(user_info.get('name'))


# def count_price_with_discount(price, discount):
#     if discount < 0 or discount > 100:
#         raise ValueError("Discount must be between 0 and 100")
    
#     discounted_price = price * (1 - discount / 100)
#     return round(discounted_price)

# count_price = count_price_with_discount(199, 20)
# print(count_price)

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