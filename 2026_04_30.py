# Валідація імені
while True:
    name = input('Please,write your Name: ')
    if len(name) <= 2:
        print('You name is very small, please write again')

    surename = input('Please,write your SureName: ')
    if  len(surename) <= 2:
        print('You SureName is very small, please write again')

    show_only_initials = input('Do you want show N.S(y/n): ').lower()

    if len(name) and len(surename) >= 2:
        break

def n_s(name:str, surename:str, type:bool):
    answer = ''
    if type == 1:
        answer = (f'{"".join(for_n_s(name))}.{"".join(for_n_s(surename))}').upper()
    elif type == 0:
        answer = name
    return answer

def for_n_s(fun: str):
    xyz = []
    for x in fun:
        xyz.append(x)
    
    return xyz[0:1]
        
def_n_s=n_s(name, surename, show_only_initials == 'y')
print(def_n_s)

# Валідація email
user_gmail = str(input("Введіть вашу електронну адресу: "))
char_gmail = []

def valid_gmail(gmail: str):
    while True:
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
                    break
                        
    answer = "Ваша електронна адреса:", "".join(char_gmail) + "@" + ".com"
    return answer
gmail = valid_gmail(user_gmail)


#Валідація пароля
number = '1234567890'
word = 'QWERTYUIOPASDFGHJKLZXCVBNM'
def valid_password(password: str):
    xyz = []
    
    answer = False
    answer_dict = {'number': False, 'word': False}
    for x in password:
        xyz.append(x)
    
    for x in xyz:
        if x in number: 
            answer_dict['number'] = True

        elif x in word:
            answer_dict['word'] = True
    return answer_dict
# encrypt_password
def for_func_password(operations: str, operand = None):
    if operand is None:
        operand = []
    for X in operations:
        operand.append(X)
    answer = operand
    return answer

def encrypt_password(password: str, key:int):

    answer = for_func_password(password)
    answer.reverse()

    word_list = for_func_password(word)
    number_list = for_func_password(number) 

    iteration = 0
    for x in password:
        iteration += 1 
        if x in word_list:
            word_list.reverse()
            answer[iteration-1] = word_list[key]

        elif x in number_list:
            number_list.reverse()
            answer[iteration-1] = number_list[key]

    return ''.join(answer)

while True:
    password = input('Please,write your Password, number symbol 8 and must have in password with numer,with up word: ')
    if len(password) >=8:
        answer_valid_password = valid_password(password)

        if answer_valid_password.get('number'):
            print('Your password is valid number')
        else: print('Your password is not valid number')

        if answer_valid_password.get('word'): 
            print('Your password is valid word')
        else: print('Your password is not valid word')

        if answer_valid_password.get('number') and answer_valid_password.get('word'):
            while True:
                key = int(input(f'Write number <= 10: '))
                if key <= 10:
                    break
                else: print('Your number is not valid')
            password_reverse_encrypt = encrypt_password(password, key)
            break
    else: print('Your password is not valid')
    
print(f'Hello {def_n_s}, your gmail:{gmail} - your password is encrypt in {password_reverse_encrypt}')