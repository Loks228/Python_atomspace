print("Welcome to the cinema!")
age_name = input("What is your age： ")
age_name = age_name.strip()

if int(age_name) < 0:
    print("Invalid age. Please enter a non-negative number.")
elif int(age_name) < 3:
    print("You are a baby, you don't need to pay.")
elif int(age_name) < 18:
    print("You are a child, you need to pay $10.")
else:
    print("You are an old man, you need to pay $15.")