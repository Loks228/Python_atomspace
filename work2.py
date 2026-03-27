students_name = ['Bob', 'Anton', 'Anna', 'Kolya', 'Dima', 'Sasha']
while input("Ви хочете видалити студента? (yes/no): ").lower() == 'yes':
    print(f"Студенти до видалення: {students_name} та іх кількість: {len(students_name)}")
    delete_student = input("Введіть ім'я студента для видалення: ")
    type_delete_student = type(delete_student)
    if type_delete_student == str:

        if delete_student in students_name:
            students_name.remove(delete_student)
            print(f"Студенти після видалення: {students_name}")

        elif delete_student not in students_name:
            print(f"Студента з ім'ям {delete_student} не знайдено в списку.")
            delete_student = int(delete_student)

        else: print("Помилка 404 ;) Спробуйте ще раз.")

    if type(delete_student) == int:

        print("Ви ввели число, тому вилення за індексом.")

        if delete_student < len(students_name):
            removed_student = students_name.pop(delete_student-1)
            print(f"Студент {removed_student} видалений. Студенти після видалення: {students_name}")
        else:
            print(f"Індекс {delete_student} виходить за межі списку студентів.")

else:
    if input("Ви вибрали не видаляти студентів! \n Хочете добавити студента? (yes/no): ") == 'yes':
        new_student = input("Введіть ім'я нового студента: ")
        students_name.append(new_student)
        print(f"Студенти після додавання: {students_name}")
    else:
        print("Ви вибрали не додавати студентів! \n Ось поточний список студентів: ")
        print(students_name)


# mid_students=len(students_name) // 2

# print(f"Три перші студенс: {students_name[0:3]}")
# print(f"Тільки першого: {students_name[0]}")
# print(f"Останній студенс {students_name[-1]}")
# print(f"Всі окрім останнього: {students_name[0:-1]}")
# print(f"Останні три: {students_name[-3:]}")
# print(f"Всі: {students_name[0:]}")
# print(f"Перша половина студентів: {students_name[0:mid_students]}")
# print(f"Друга половина студентів: {students_name[mid_students:]}")

