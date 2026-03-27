#
YEARS_OLD = int(input("How many years old are you? "))
months_old = YEARS_OLD * 12
weeks_old = YEARS_OLD * 52
days_old = YEARS_OLD * 365
hours_old = days_old * 24
print(f"You are: \n- {YEARS_OLD} years old.")
print(f"- {months_old} months old.")
print(f"- {weeks_old} weeks old.")
print(f"- {days_old} days old.")
print(f"- {hours_old} hours old.")