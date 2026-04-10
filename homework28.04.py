numbers = [1, 2, 3, 4, 5]

new_number = int(input("Введіть число: "))

# перевірка
if new_number in numbers:
    print("Таке число вже є в списку")
else:
    numbers.append(new_number)
    print("Число додано")

print("Список:", numbers)