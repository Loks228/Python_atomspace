
DOLLAR = 43.84
EURO = 50.74

class CurrencyConverter:

    def convert_to_dollar(amount):
        print(f"Converting {amount} to dollars...")
        return amount / 43.84
    
    def convert_to_euro(amount):
        print(f"Converting {amount} to euros...")
        return amount / 50.74
    
if __name__ == "__main__":
    amount = float(input("Enter the amount in your local currency: "))
    print(f"{amount} in dollars is: {CurrencyConverter.convert_to_dollar(amount)}")
    print(f"{amount} in euros is: {CurrencyConverter.convert_to_euro(amount)}")